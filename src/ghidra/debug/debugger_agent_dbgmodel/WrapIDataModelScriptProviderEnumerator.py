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
package agent.dbgmodel.jna.dbgmodel.datamodel.script;

import com.sun.jna.Pointer;
import com.sun.jna.Structure;
import com.sun.jna.platform.win32.WinNT.HRESULT;
import com.sun.jna.ptr.PointerByReference;

import agent.dbgmodel.jna.dbgmodel.UnknownWithUtils;

public class WrapIDataModelScriptProviderEnumerator extends UnknownWithUtils
		implements IDataModelScriptProviderEnumerator {
	public static class ByReference extends WrapIDataModelScriptProviderEnumerator
			implements Structure.ByReference {
	}

	public WrapIDataModelScriptProviderEnumerator() {
	}

	public WrapIDataModelScriptProviderEnumerator(Pointer pvInstance) {
		super(pvInstance);
	}

	@Override
	public HRESULT Reset() {
		return _invokeHR(VTIndices.RESET, getPointer());
	}

	@Override
	public HRESULT GetNext(PointerByReference provider) {
		return _invokeHR(VTIndices.GET_NEXT, getPointer(), provider);
	}

}
