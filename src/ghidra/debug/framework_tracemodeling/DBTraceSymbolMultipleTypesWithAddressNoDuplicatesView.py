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
package ghidra.trace.database.symbol;

import java.util.Collection;

import ghidra.trace.model.symbol.TraceSymbolWithAddressNoDuplicatesView;

public class DBTraceSymbolMultipleTypesWithAddressNoDuplicatesView<T extends AbstractDBTraceSymbol>
		extends DBTraceSymbolMultipleTypesWithAddressView<T>
		implements TraceSymbolWithAddressNoDuplicatesView<T> {

	public DBTraceSymbolMultipleTypesWithAddressNoDuplicatesView(DBTraceSymbolManager manager,
			Collection<? extends AbstractDBTraceSymbolSingleTypeWithAddressView<? extends T>> parts) {
		super(manager, parts);
	}

	@SafeVarargs
	public DBTraceSymbolMultipleTypesWithAddressNoDuplicatesView(DBTraceSymbolManager manager,
			AbstractDBTraceSymbolSingleTypeWithAddressView<? extends T>... parts) {
		super(manager, parts);
	}
}
