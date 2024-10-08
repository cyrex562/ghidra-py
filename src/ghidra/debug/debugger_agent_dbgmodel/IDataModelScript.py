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
import com.sun.jna.WString;
import com.sun.jna.platform.win32.Guid.IID;
import com.sun.jna.platform.win32.WTypes.BSTRByReference;
import com.sun.jna.platform.win32.WinDef.BOOLByReference;
import com.sun.jna.platform.win32.WinNT.HRESULT;

import agent.dbgmodel.jna.dbgmodel.IUnknownEx;
import agent.dbgmodel.jna.dbgmodel.UnknownWithUtils.VTableIndex;

public interface IDataModelScript extends IUnknownEx {
	final IID IID_IDATA_MODEL_SCRIPT = new IID("7B4D30FC-B14A-49f8-8D87-D9A1480C97F7");

	enum VTIndices implements VTableIndex {
		GET_NAME, //
		RENAME, //
		POPULATE, //
		EXECUTE, //
		UNLINK, //
		IS_INVOCABLE, //
		INVOKE_MAIN, //
		;

		static int start = 3;

		@Override
		public int getIndex() {
			return this.ordinal() + start;
		}
	}

	HRESULT GetName(BSTRByReference scriptName);

	HRESULT Rename(WString scriptName);

	HRESULT Populate(Pointer contentStream);

	HRESULT Execute(Pointer client);

	HRESULT Unlink();

	HRESULT IsInvocable(BOOLByReference isInvocable);

	HRESULT InvokeMain(Pointer client);

}
