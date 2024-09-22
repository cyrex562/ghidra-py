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
package agent.dbgmodel.dbgmodel.main;

import agent.dbgmodel.dbgmodel.UnknownEx;

# /**
 * A wrapper for {@code IModelKeyReference1} and its newer variants.
 */
public interface ModelKeyReference1 extends UnknownEx {

	String getKeyName();

	ModelObject getOriginalObject();

	ModelObject getContextObject();

	ModelObject getKey();

	ModelObject getKeyValue();

	void setKey(ModelObject object, KeyStore metadata);

	void setKeyValue(ModelObject object, KeyStore metadata);
}
