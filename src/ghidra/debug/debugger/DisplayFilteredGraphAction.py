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
package ghidra.app.plugin.core.debug.gui.objects.actions;

import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;
import java.util.List;
import java.util.Set;

import javax.swing.Icon;

import docking.action.KeyBindingData;
import docking.action.MenuData;
import generic.theme.GIcon;
import ghidra.app.plugin.core.debug.gui.objects.DebuggerObjectsProvider;
import ghidra.app.plugin.core.debug.gui.objects.ObjectContainer;
import ghidra.app.services.GraphDisplayBroker;
import ghidra.framework.plugintool.PluginTool;
import ghidra.service.graph.*;
import ghidra.util.HelpLocation;
import ghidra.util.Msg;
import ghidra.util.exception.CancelledException;
import ghidra.util.exception.GraphException;
import ghidra.util.task.TaskMonitor;

public class DisplayFilteredGraphAction extends DisplayFilteredAction {

	protected GraphDisplayBroker graphBroker;

	protected static final Icon ICON_GRAPH = new GIcon("icon.debugger.display.xml.filtered");

	public DisplayFilteredGraphAction(PluginTool tool, String owner,
			DebuggerObjectsProvider provider) {
		super("DisplayFilteredGraph", tool, owner, provider);
		String[] path = new String[] { "Display filtered...", "Graph" };
		setPopupMenuData(new MenuData(path, ICON_GRAPH));
		setKeyBindingData(new KeyBindingData(KeyEvent.VK_G,
			InputEvent.CTRL_DOWN_MASK | InputEvent.SHIFT_DOWN_MASK));
		setHelpLocation(new HelpLocation(owner, "display_filtered_graph"));
		provider.addLocalAction(this);
	}

	@Override
	protected void doAction(ObjectContainer container, List<String> path) {
		graphBroker = provider.getGraphBroker();
		if (graphBroker == null) {
			Msg.showError(this, tool.getToolFrame(), "DisplayAsGraph Error",
				"GraphBroker not found: Please add a graph provider to your tool");
			return;
		}
		ObjectContainer clone = ObjectContainer.clone(container);
		clone.setImmutable(true);
		getOffspring(clone, path);
	}

	private void graphContainer(ObjectContainer container, AttributedGraph graph,
			AttributedVertex start) {
		Set<ObjectContainer> children = container.getCurrentChildren();
		for (ObjectContainer c : children) {
			AttributedVertex end = graph.addVertex(c.getName(), c.toString());
			graph.addEdge(start, end, c.getTargetObject().getName());
			if (c.hasElements()) {
				graphContainer(c, graph, end);
			}
		}
	}

	@Override
	protected void finishGetOffspring(ObjectContainer container, final List<String> path) {
		GraphDisplayProvider graphProvider = graphBroker.getDefaultGraphDisplayProvider();
		AttributedGraph graph = new AttributedGraph(container.getName(), new EmptyGraphType());
		AttributedVertex start = graph.addVertex(container.getName(), container.toString());
		graphContainer(container, graph, start);
		try {
			GraphDisplay graphDisplay = graphProvider.getGraphDisplay(true, TaskMonitor.DUMMY);
			graphDisplay.setGraph(graph, container.getName(), false, TaskMonitor.DUMMY);
		}
		catch (GraphException e) {
			e.printStackTrace();
		}
		catch (CancelledException e) {
			//DO NOTHING
		}
	}
}
