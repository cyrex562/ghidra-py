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

import generic.lsh.vector.LSHVectorFactory;
import ghidra.features.bsim.query.LSHException;
import ghidra.features.bsim.query.description.DatabaseInformation;
import ghidra.xml.XmlElement;
import ghidra.xml.XmlPullParser;

public class CreateDatabase extends BSimQuery<ResponseInfo> {
	public String config_template;			// Name of configuration to use for database
	public DatabaseInformation info;				// Some overrides for the configuration
	public ResponseInfo inforesponse;
	
	public CreateDatabase() {
		super("createdatabase");
	}
	
	@Override
	public void buildResponseTemplate() {
		if (response == null)
			response = inforesponse = new ResponseInfo();
	}

	@Override
	public void saveXml(Writer fwrite) throws IOException {
		fwrite.append('<').append(name);
		fwrite.append(" template=\"").append(config_template).append("\">\n");
		info.saveXml(fwrite);
		fwrite.append("</").append(name).append(">\n");
	}

	@Override
	public void restoreXml(XmlPullParser parser, LSHVectorFactory vectorFactory) throws LSHException {
		XmlElement el = parser.start(name);
		config_template = el.getAttribute("template");
		info = new DatabaseInformation();
		info.restoreXml(parser);
		parser.end();
	}

}
