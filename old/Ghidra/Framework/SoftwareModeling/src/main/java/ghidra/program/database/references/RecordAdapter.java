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
package ghidra.program.database.references;



import db.DBRecord;

interface RecordAdapter {

	public DBRecord createRecord(long key, int numRefs, byte refLevel, byte[] refData)
			throws IOException;

	public DBRecord getRecord(long key) throws IOException;

	/**
	 * @param key
	 * @param refData
	 */
	public void putRecord(DBRecord record) throws IOException;

	/**
	 * @param key
	 */
	public void removeRecord(long key) throws IOException;

}
