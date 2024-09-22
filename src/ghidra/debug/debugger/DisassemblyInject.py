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
package ghidra.app.plugin.core.debug.disassemble;

import ghidra.app.plugin.core.debug.disassemble.DisassemblyInjectInfo.PlatformInfo;
import ghidra.debug.api.platform.DebuggerPlatformMapper;
import ghidra.framework.plugintool.PluginTool;
import ghidra.program.model.address.AddressSetView;
import ghidra.trace.model.guest.TracePlatform;
import ghidra.trace.model.thread.TraceThread;
import ghidra.util.Msg;
import ghidra.util.classfinder.ExtensionPoint;

# /**
 * A configuration inject for automatic disassembly at the program counter
 * 
 * <p>
 * Ghidra uses a "context register" to control the modes of disassembly for certain processor
 * languages. Debuggers don't have such a context register, but may have access to the various
 * status registers actually used by that processor to select, e.g., an ISA. These injects "glue"
 * the disassembler to context derived from status registers. Each supported context-sensitive
 * processor will likely need its own inject; thus, these are pluggable extensions. It's unlikely
 * multiple injects should ever be needed, but it is supported, just in case. The injects are
 * invoked in order of priority, starting with the least. Since injects are meant simply to
 * configure the disassembler (namely seeding its context), the one invoked last will have "the last
 * word." As such, each inject should avoid unnecessarily erasing existing context.
 */
@DisassemblyInjectInfo(platforms = {}) // Use as default
public interface DisassemblyInject extends ExtensionPoint {
	/**
	 * If present, get the information annotation on this inject
	 * 
	 * @return the info
	 */
	default DisassemblyInjectInfo getInfo() {
		DisassemblyInjectInfo info = getClass().getAnnotation(DisassemblyInjectInfo.class);
		if (info == null) {
			Msg.warn(this, getClass() + " is missing @" +
				DisassemblyInjectInfo.class.getSimpleName() + " annotation");
			return DisassemblyInject.class.getAnnotation(DisassemblyInjectInfo.class);
		}
		return info;
	}

	/**
	 * Check if this inject applies to the given trace platform
	 * 
	 * @param platform the platform to check
	 * @return true if applicable, false otherwise
	 */
	default boolean isApplicable(TracePlatform platform) {
		for (PlatformInfo info : getInfo().platforms()) {
			if (info.langID().equals(platform.getLanguage().getLanguageID().toString())) {
				if (info.compilerID().isBlank() || info.compilerID()
						.equals(platform.getCompilerSpec().getCompilerSpecID().toString())) {
					return true;
				}
			}
		}
		return false;
	}

	/**
	 * Get this injects position in the invocation order
	 * 
	 * @return the priority
	 */
	default int getPriority() {
		return getInfo().priority();
	}

	/**
	 * A pre-auto disassembly hook
	 * 
	 * <p>
	 * This hook is invoked by the {@link DebuggerPlatformMapper} before disassembly actually
	 * begins. The callback occurs within the command's background thread. In general, the inject
	 * should limit its operation to inspecting the trace database and configuring the command.
	 * 
	 * @param tool the tool that will execute the command
	 * @param command the command to be configured, which is about to execute
	 * @param platform the trace platform for the disassembler
	 * @param snap the snap the snap at which to disassemble
	 * @param thread the thread whose PC is being disassembled
	 * @param startSet the starting address set, usually just the PC
	 * @param restricted the set of disassemblable addresses
	 */
	default void pre(PluginTool tool, TraceDisassembleCommand command, TracePlatform platform,
			long snap, TraceThread thread, AddressSetView startSet, AddressSetView restricted) {
	}

	/**
	 * A post-auto disassembly hook
	 * 
	 * <p>
	 * This hook is invoked by the {@link DebuggerPlatformMapper} after disassembly completes. The
	 * callback occurs within the command's background thread.
	 * 
	 * @param tool the tool that just executed the disassembly command
	 * @param platform the trace platform for the disassembler
	 * @param snap the snap the snap at which disassembly was performed
	 * @param disassembled the addresses that were actually disassembled
	 */
	default void post(PluginTool tool, TracePlatform platform, long snap,
			AddressSetView disassembled) {
	}
}
