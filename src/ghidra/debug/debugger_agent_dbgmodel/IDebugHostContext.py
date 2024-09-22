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
package agent.dbgmodel.jna.dbgmodel.debughost;

import com.sun.jna.Pointer;
import com.sun.jna.platform.win32.Guid.IID;
import com.sun.jna.platform.win32.WinDef.BOOLByReference;
import com.sun.jna.platform.win32.WinNT.HRESULT;

import agent.dbgmodel.jna.dbgmodel.IUnknownEx;
import agent.dbgmodel.jna.dbgmodel.UnknownWithUtils.VTableIndex;

public interface IDebugHostContext extends IUnknownEx {
	final IID IID_IDEBUG_HOST_CONTEXT = new IID("A68C70D8-5EC0-46e5-B775-3134A48EA2E3");

	enum VTIndices implements VTableIndex {
		IS_EQUAL_TO, //
		;

		static int start = 3;

		@Override
		public int getIndex() {
			return this.ordinal() + start;
		}
	}

	HRESULT IsEqualTo(Pointer pContext, BOOLByReference pIsEqual);

}
