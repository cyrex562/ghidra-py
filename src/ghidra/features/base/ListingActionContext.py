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
package ghidra.app.context;

import docking.ComponentProvider;
import ghidra.app.nav.Navigatable;
import ghidra.program.model.listing.Program;
import ghidra.program.util.ProgramLocation;
import ghidra.program.util.ProgramSelection;

public class ListingActionContext extends NavigatableActionContext {

	public ListingActionContext(ComponentProvider provider, Navigatable navigatable) {
		super(provider, navigatable);
	}

	public ListingActionContext(ComponentProvider provider, Navigatable navigatable,
			ProgramLocation location) {
		super(provider, navigatable, location);
	}

	public ListingActionContext(ComponentProvider provider, Navigatable navigatable,
			Program program, ProgramLocation location, ProgramSelection selection,
			ProgramSelection highlight) {
		super(provider, navigatable, program, location, selection, highlight);
	}
}
