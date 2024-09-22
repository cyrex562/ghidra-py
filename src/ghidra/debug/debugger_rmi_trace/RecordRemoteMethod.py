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
package ghidra.app.plugin.core.debug.service.tracermi;

import java.util.Map;

import ghidra.dbg.target.schema.TargetObjectSchema.SchemaName;
import ghidra.debug.api.target.ActionName;
import ghidra.debug.api.tracermi.*;
import ghidra.trace.model.Trace;

public record RecordRemoteMethod(TraceRmiHandler handler, String name, ActionName action,
		String display, String description, Map<String, RemoteParameter> parameters,
		SchemaName retType) implements RemoteMethod {
	@Override
	public DefaultRemoteAsyncResult invokeAsync(Map<String, Object> arguments) {
		Trace trace = validate(arguments);
		OpenTrace open = handler.getOpenTrace(trace);
		return handler.invoke(open, name, arguments);
	}
}
