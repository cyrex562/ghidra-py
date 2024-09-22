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
package ghidra.app.plugin.core.debug.gui.control;

import java.awt.event.KeyEvent;

import javax.swing.Icon;
import javax.swing.KeyStroke;

import ghidra.app.plugin.core.debug.gui.DebuggerResources;
import ghidra.debug.api.target.ActionName;
import ghidra.util.HelpLocation;

interface TargetStepOverAction extends ControlAction {
	String NAME = "Step Over";
	String DESCRIPTION = "Step the target over";
	Icon ICON = DebuggerResources.ICON_STEP_OVER;
	String HELP_ANCHOR = "target_step_over";
	int SUB_GROUP = 6;
	KeyStroke KEY_BINDING = KeyStroke.getKeyStroke(KeyEvent.VK_F10, 0);

	static TargetActionBuilder builder(DebuggerControlPlugin owner) {
		String ownerName = owner.getName();
		return new TargetActionBuilder(NAME, owner)
				.action(ActionName.STEP_OVER)
				.toolBarIcon(ICON)
				.toolBarGroup(GROUP, ControlAction.intSubGroup(SUB_GROUP))
				.keyBinding(KEY_BINDING)
				.defaultDescription(DESCRIPTION)
				.helpLocation(new HelpLocation(ownerName, HELP_ANCHOR));
	}
}
