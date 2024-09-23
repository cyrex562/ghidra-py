/* ###
 * IP: GHIDRA
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package ghidra.trace.database.time;


import java.util.Collection;
import java.util.Collections;
import java.util.Map.Entry;
import java.util.concurrent.locks.ReadWriteLock;

import db.DBHandle;
import ghidra.framework.data.OpenMode;
import ghidra.trace.database.DBTrace;
import ghidra.trace.database.DBTraceManager;
import ghidra.trace.database.thread.DBTraceThreadManager;
import ghidra.trace.model.time.TraceSnapshot;
import ghidra.trace.model.time.TraceTimeManager;
import ghidra.trace.model.time.schedule.TraceSchedule;
import ghidra.trace.util.TraceChangeRecord;
import ghidra.trace.util.TraceEvents;
import ghidra.util.LockHold;
import ghidra.util.database.*;
import ghidra.util.exception.VersionException;
import ghidra.util.task.TaskMonitor;

public class DBTraceTimeManager implements TraceTimeManager, DBTraceManager {

	protected final ReadWriteLock lock;
	protected final DBTrace trace;
	protected final DBTraceThreadManager threadManager;

	protected final DBCachedObjectStore<DBTraceSnapshot> snapshotStore;
	protected final DBCachedObjectIndex<String, DBTraceSnapshot> snapshotsBySchedule;

	public DBTraceTimeManager(DBHandle dbh, OpenMode openMode, ReadWriteLock lock,
			TaskMonitor monitor, DBTrace trace, DBTraceThreadManager threadManager)
			throws VersionException, IOException {
		this.trace = trace;
		this.lock = lock;
		this.threadManager = threadManager;

		DBCachedObjectStoreFactory factory = trace.getStoreFactory();

		snapshotStore = factory.getOrCreateCachedStore(DBTraceSnapshot.TABLE_NAME,
			DBTraceSnapshot.class, (s, r) -> new DBTraceSnapshot(this, s, r), true);
		snapshotsBySchedule = snapshotStore.getIndex(String.class, DBTraceSnapshot.SCHEDULE_COLUMN);
	}

	@Override
	public void dbError(IOException e) {
		trace.dbError(e);
	}

	@Override
	public void invalidateCache(boolean all) {
		snapshotStore.invalidateCache();
	}

	protected void notifySnapshotAdded(DBTraceSnapshot snapshot) {
		trace.updateViewportsSnapshotAdded(snapshot);
		trace.setChanged(new TraceChangeRecord<>(TraceEvents.SNAPSHOT_ADDED, null, snapshot));
	}

	protected void notifySnapshotChanged(DBTraceSnapshot snapshot) {
		trace.updateViewportsSnapshotChanged(snapshot);
		trace.setChanged(new TraceChangeRecord<>(TraceEvents.SNAPSHOT_CHANGED, null, snapshot));
	}

	protected void notifySnapshotDeleted(DBTraceSnapshot snapshot) {
		trace.updateViewportsSnapshotDeleted(snapshot);
		trace.setChanged(new TraceChangeRecord<>(TraceEvents.SNAPSHOT_DELETED, null, snapshot));
	}

	@Override
	public DBTraceSnapshot createSnapshot(String description) {
		try (LockHold hold = LockHold.lock(lock.writeLock())) {
			DBTraceSnapshot snapshot = snapshotStore.create();
			snapshot.set(System.currentTimeMillis(), description);
			if (snapshot.getKey() == 0) {
				// Convention for first snap
				snapshot.setSchedule(TraceSchedule.snap(0));
			}
			notifySnapshotAdded(snapshot);
			return snapshot;
		}
	}

	@Override
	public DBTraceSnapshot getSnapshot(long snap, boolean createIfAbsent) {
		if (!createIfAbsent) {
			try (LockHold hold = LockHold.lock(lock.readLock())) {
				return snapshotStore.getObjectAt(snap);
			}
		}
		try (LockHold hold = LockHold.lock(lock.writeLock())) {
			DBTraceSnapshot snapshot = snapshotStore.getObjectAt(snap);
			if (snapshot == null) {
				snapshot = snapshotStore.create(snap);
				snapshot.set(System.currentTimeMillis(), "");
				if (snapshot.getKey() == 0) {
					// Convention for first snap
					snapshot.setSchedule(TraceSchedule.snap(0));
				}
				notifySnapshotAdded(snapshot);
			}
			return snapshot;
		}
	}

	@Override
	public DBTraceSnapshot getMostRecentSnapshot(long snap) {
		try (LockHold hold = LockHold.lock(lock.readLock())) {
			Entry<Long, DBTraceSnapshot> ent = snapshotStore.asMap().floorEntry(snap);
			return ent == null ? null : ent.getValue();
		}
	}

	@Override
	public Collection<? extends TraceSnapshot> getSnapshotsWithSchedule(TraceSchedule schedule) {
		return snapshotsBySchedule.get(schedule.toString());
	}

	@Override
	public Collection<? extends DBTraceSnapshot> getAllSnapshots() {
		return Collections.unmodifiableCollection(snapshotStore.asMap().values());
	}

	@Override
	public Collection<? extends DBTraceSnapshot> getSnapshots(long fromSnap, boolean fromInclusive,
			long toSnap, boolean toInclusive) {
		return Collections.unmodifiableCollection(
			snapshotStore.asMap().subMap(fromSnap, fromInclusive, toSnap, toInclusive).values());
	}

	@Override
	public Long getMaxSnap() {
		return snapshotStore.getMaxKey();
	}

	@Override
	public long getSnapshotCount() {
		return snapshotStore.getRecordCount();
	}

	public void deleteSnapshot(DBTraceSnapshot snapshot) {
		try (LockHold hold = LockHold.lock(lock.writeLock())) {
			snapshotStore.delete(snapshot);
			notifySnapshotDeleted(snapshot);
		}
	}
}
