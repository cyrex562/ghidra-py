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
package agent.dbgeng.jna.dbgeng.client;

import com.sun.jna.Pointer;
import com.sun.jna.Structure;
import com.sun.jna.platform.win32.WinDef.ULONG;
import com.sun.jna.platform.win32.WinNT.HRESULT;

# /**
 * Wrapper class for the IDebugClient interface
 */
public class WrapIDebugClient7 extends WrapIDebugClient6 implements IDebugClient7 {
	public static class ByReference extends WrapIDebugClient7 implements Structure.ByReference {
	}

	public WrapIDebugClient7() {
	}

	public WrapIDebugClient7(Pointer pvInstance) {
		super(pvInstance);
	}

	@Override
	public HRESULT SetClientContext(Pointer Context, ULONG ContextSize) {
		return _invokeHR(VTIndices7.SET_CLIENT_CONTEXT, getPointer(), Context, ContextSize);
	}
}
