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
package agent.dbgeng.manager;

import java.math.BigInteger;
import java.util.concurrent.CompletableFuture;

public interface DbgStackFrame extends DbgStackFrameOperations {

	/**
	 * Get the address of the program counter
	 * 
	 * @return the program counter
	 */
	BigInteger getAddress();

	/**
	 * Get the name of the function where the program counter is
	 * 
	 * @return the function name
	 */
	String getFunction();

	/**
	 * Get the level of the frame
	 * 
	 * Frame 0 is the actual machine state, and each increment unwinds the stack 1 frame.
	 * 
	 * @return the frame level
	 */
	int getLevel();

	/**
	 * Make this frame the current frame
	 * 
	 * @return a future that completes when the frame is the current frame
	 */
	CompletableFuture<Void> setActive();

	/**
	 * Get the thread for this frame
	 * 
	 * @return the thread
	 */
	DbgThread getThread();

	long getFuncTableEntry();

	long getFrameOffset();

	long getReturnOffset();

	long getStackOffset();

	boolean getVirtual();

	long[] getParams();
}
