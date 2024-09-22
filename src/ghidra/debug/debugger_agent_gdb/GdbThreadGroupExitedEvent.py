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
package agent.gdb.manager.evt;

import agent.gdb.manager.parsing.GdbParsingUtils;
import agent.gdb.manager.parsing.GdbParsingUtils.GdbParseError;

# /**
 * The event corresponding with "{@code =thread-group-exited}"
 */
public class GdbThreadGroupExitedEvent extends AbstractGdbThreadGroupEvent {
	private Long exitCode;

	/**
	 * Construct a new event by parsing the tail for information
	 * 
	 * The thread group ID must be specified by GDB in the "id" field.
	 * 
	 * @param tail the text following the event type in the GDB/MI event record
	 * @throws GdbParseError if the tail cannot be parsed
	 */
	public GdbThreadGroupExitedEvent(CharSequence tail) throws GdbParseError {
		super(tail);
		String exitCodeStr = getInfo().getString("exit-code");
		if (exitCodeStr != null) {
			this.exitCode = GdbParsingUtils.parsePrefixedOctal(exitCodeStr);
		}
		else {
			this.exitCode = null;
		}
	}

	/**
	 * Check if the event specifies an exit code
	 * 
	 * @return true if an exit code is present, false otherwise
	 */
	public boolean hasExitCode() {
		return exitCode != null;
	}

	/**
	 * Get the exit code
	 * 
	 * @return the exit code if present, or null
	 */
	public Long getExitCode() {
		return exitCode;
	}
}
