/* ###
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
package ghidra.pty.linux;

import static org.junit.Assume.assumeTrue;



import org.junit.Before;

import ghidra.framework.OperatingSystem;
import ghidra.pty.unix.AbstractUnixPtyTest;
import ghidra.pty.unix.UnixPty;

public class LinuxPtyTest extends AbstractUnixPtyTest {
	@Before
	public void checkLinux() {
		assumeTrue(OperatingSystem.LINUX == OperatingSystem.CURRENT_OPERATING_SYSTEM);
	}

	@Override
	protected UnixPty openpty() throws IOException {
		return UnixPty.openpty(LinuxIoctls.INSTANCE);
	}
}
