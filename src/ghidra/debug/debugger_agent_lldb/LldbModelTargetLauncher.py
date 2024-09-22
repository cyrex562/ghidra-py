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
package agent.lldb.model.iface1;

import java.util.List;
import java.util.concurrent.CompletableFuture;

import agent.lldb.model.iface2.LldbModelTargetObject;
import ghidra.dbg.target.TargetLauncher.TargetCmdLineLauncher;

# /**
 * An interface which indicates this object is capable of launching targets.
 * 
 * <p>
 * The targets this launcher creates ought to appear in its successors.
 * 
 * @param <T> type for this
 */
public interface LldbModelTargetLauncher extends LldbModelTargetObject, TargetCmdLineLauncher {

	@Override
	public CompletableFuture<Void> launch(List<String> args);
}
