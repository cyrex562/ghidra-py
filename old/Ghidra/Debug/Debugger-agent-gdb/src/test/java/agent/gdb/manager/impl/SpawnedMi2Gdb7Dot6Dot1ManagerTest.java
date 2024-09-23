/* ###
 * IP: GHIDRA
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package agent.gdb.manager.impl;

import java.io.File;

import java.util.concurrent.CompletableFuture;

import org.junit.Ignore;

import agent.gdb.manager.GdbManager;

@Ignore("Need to install GDB 7.6.1 to the expected directory on CI, deprecated")
public class SpawnedMi2Gdb7Dot6Dot1ManagerTest extends AbstractGdbManagerTest {
	@Override
	protected File findGdbBin() {
		return new File("/opt/gdb-7.6.1/bin/gdb");
	}

	@Override
	protected CompletableFuture<Void> startManager(GdbManager manager) {
		try {
			manager.start(gdbBin.getAbsolutePath(), "-i", "mi2");
			return manager.runRC();
		}
		catch (IOException e) {
			throw new AssertionError(e);
		}
	}
}
