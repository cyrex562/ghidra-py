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
package ghidra.app.util.bin.format.golang.structmapping;

import static java.lang.annotation.ElementType.FIELD;
import static java.lang.annotation.ElementType.METHOD;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

import java.lang.annotation.Retention;
import java.lang.annotation.Target;

# /**
 * Indicates that the objects in the return value of the tagged method should be recursively
 * marked up, or if a tagged field, the object in the field should be recursively marked up.
 * <p>
 * The return value can be an object with {@link StructureMapping} info, or a 
 * collection / iterator of those objects.
 */
@Retention(RUNTIME)
@Target({ FIELD, METHOD })
public @interface Markup {
	// nothing
}
