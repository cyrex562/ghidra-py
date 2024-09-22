# /* ###
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
package sarif.export.extlib;

import ghidra.program.model.data.ISF.IsfObject;
import ghidra.program.model.symbol.SourceType;

public class ExtLibrary implements IsfObject {

	public String name;
	public String location;
	public String sourceType;
	
	public ExtLibrary(String name, String path, SourceType sourceType) {
		this.name = name;
		location = path;
		this.sourceType = sourceType.toString();
	}

}
