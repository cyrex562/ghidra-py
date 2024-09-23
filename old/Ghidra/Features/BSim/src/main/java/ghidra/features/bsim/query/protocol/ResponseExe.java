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
package ghidra.features.bsim.query.protocol;


import java.io.Writer;
import java.util.ArrayList;
import java.util.List;

import generic.lsh.vector.LSHVectorFactory;
import ghidra.features.bsim.query.LSHException;
import ghidra.features.bsim.query.description.DescriptionManager;
import ghidra.features.bsim.query.description.ExecutableRecord;
import ghidra.features.bsim.query.ingest.BulkSignatures;
import ghidra.xml.XmlPullParser;

/**
 * Response to a request for executables from a {@link BulkSignatures} call.
 *
 */
public class ResponseExe extends QueryResponseRecord {

	public List<ExecutableRecord> records;
	public DescriptionManager manage;
	public int recordCount = 0;

	/**
	 * Constructor.
	 */
	public ResponseExe() {
		super("responsexe");
		manage = new DescriptionManager();
		records = new ArrayList<>();
	}

	@Override
	public DescriptionManager getDescriptionManager() {
		return manage;
	}

	@Override
	public void saveXml(Writer fwrite) throws IOException {
		// no need to implement
	}

	@Override
	public void restoreXml(XmlPullParser parser, LSHVectorFactory vectorFactory)
			throws LSHException {
		// no need to implement
	}
}
