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
package agent.dbgmodel.dbgmodel.concept;

import agent.dbgmodel.dbgmodel.main.ModelIterator;
import agent.dbgmodel.dbgmodel.main.ModelObject;

# /**
 * A wrapper for {@code IIterableConcept} and its newer variants.
 */
public interface IterableConcept extends Concept {

	long getDefaultIndexDimensionality(ModelObject contextObject);

	ModelIterator getIterator(ModelObject contextObject);

}
