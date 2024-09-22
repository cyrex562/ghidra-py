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
package ghidra.app.plugin.core.decompile;

import java.util.function.Supplier;

import docking.ActionContext;
import docking.action.DockingActionIf;
import ghidra.app.context.NavigatableActionContext;
import ghidra.app.context.RestrictedAddressSetContext;
import ghidra.app.decompiler.*;
import ghidra.app.decompiler.component.DecompilerPanel;
import ghidra.framework.plugintool.PluginTool;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.pcode.HighFunction;
import ghidra.util.Msg;
import ghidra.util.UndefinedFunction;
import utility.function.Callback;

public class DecompilerActionContext extends NavigatableActionContext
		implements RestrictedAddressSetContext {
	private final Address functionEntryPoint;
	private final boolean isDecompiling;
	private final int lineNumber;

	private ClangToken tokenAtCursor = null;
	private boolean tokenIsInitialized = false;

	/**
	 * Construct a context specifying the line number
	 * 
	 * <p>
	 * The specified line number may not necessarily correspond to that of the current token. This
	 * is usually the case when the user clicks somewhere where a token is not present, e.g., the
	 * margin. In these cases, the line number should be that under the mouse cursor.
	 * 
	 * @param provider the decompiler provider producing the context
	 * @param functionEntryPoint the current function's entry, if applicable
	 * @param isDecompiling true if the decompiler is still working
	 * @param lineNumber non-zero to specify the line number
	 */
	public DecompilerActionContext(DecompilerProvider provider, Address functionEntryPoint,
			boolean isDecompiling, int lineNumber) {
		super(provider, provider);
		if (lineNumber < 0) {
			throw new IllegalArgumentException("lineNumber must be >= 0. Got " + lineNumber);
		}
		this.functionEntryPoint = functionEntryPoint;
		this.isDecompiling = isDecompiling;
		this.lineNumber = lineNumber;
	}

	/**
	 * Construct a context using the current token's line number
	 * 
	 * @param provider the decompiler provider producing the context
	 * @param functionEntryPoint the current function's entry, if applicable
	 * @param isDecompiling true if the decompiler is still working
	 */
	public DecompilerActionContext(DecompilerProvider provider, Address functionEntryPoint,
			boolean isDecompiling) {
		this(provider, functionEntryPoint, isDecompiling, 0);
	}

	public Address getFunctionEntryPoint() {
		return functionEntryPoint;
	}

	public boolean isDecompiling() {
		return isDecompiling;
	}

	@Override
	public DecompilerProvider getComponentProvider() {
		return (DecompilerProvider) super.getComponentProvider();
	}

	public PluginTool getTool() {
		return getComponentProvider().getTool();
	}

	public ClangToken getTokenAtCursor() {
		if (!tokenIsInitialized) {
			tokenAtCursor = getDecompilerPanel().getTokenAtCursor();
			tokenIsInitialized = true;
		}
		return tokenAtCursor;
	}

	/**
	 * Get the line number
	 * 
	 * <p>
	 * This may not always correspond to the line number of the token at the cursor. For example, if
	 * there is no token under the mouse, or if the context is produced by the margin. When
	 * generated by a mouse event, this is the line number determined by the mouse's vertical
	 * position. Otherwise, this is the line number of the current token. If there is no current
	 * token and the line number was not given at construction, this returns 0 to indicate this
	 * context has no line number.
	 * 
	 * <p>
	 * If the current token's line number is desired, regardless of the user's mouse position, then
	 * use {@code context.}{@link #getTokenAtCursor()}{@code .}{@link ClangToken#getLineParent()
	 * getLineParent()}{@code .}{@link ClangLine#getLineNumber() getLineNumber()}.
	 * 
	 * @return the line number
	 */
	public int getLineNumber() {
		if (lineNumber != 0) {
			return lineNumber;
		}
		getTokenAtCursor();
		return tokenAtCursor == null ? 0 : tokenAtCursor.getLineParent().getLineNumber();
	}

	public DecompilerPanel getDecompilerPanel() {
		return getComponentProvider().getDecompilerPanel();
	}

	public Function getFunction() {
		return getComponentProvider().getController().getFunction();
	}

	public HighFunction getHighFunction() {
		return getComponentProvider().getController().getHighFunction();
	}

	public ClangTokenGroup getCCodeModel() {
		return getComponentProvider().getController().getCCodeModel();
	}

	public boolean hasRealFunction() {
		Function f = getFunction();
		return f != null && !(f instanceof UndefinedFunction);
	}

	public void setStatusMessage(String msg) {
		getComponentProvider().getController().setStatusMessage(msg);
	}

	/**
	 * The companion method of {@link #checkActionEnablement(Supplier)}.
	 * 
	 * <p>
	 * Decompiler actions must call this method from their
	 * {@link DockingActionIf#actionPerformed(ActionContext)} if they require state from the
	 * Decompiler.
	 * 
	 * @param actionCallback the action's code to execute
	 */
	public void performAction(Callback actionCallback) {

		if (isDecompiling) {
			Msg.showInfo(getClass(), getComponentProvider().getComponent(),
				"Decompiler Action Blocked",
				"You cannot perform Decompiler actions while the Decompiler is busy");
			return;
		}

		actionCallback.call();
	}

	/**
	 * The companion method of {@link #performAction(Callback)}.
	 * 
	 * <p>
	 * Decompiler actions must call this method from their
	 * {@link DockingActionIf#isEnabledForContext(ActionContext)} if they require state from the
	 * Decompiler.
	 * 
	 * @param actionBooleanSupplier the action's code to verify its enablement
	 * @return true if the action should be considered enabled
	 */
	public boolean checkActionEnablement(Supplier<Boolean> actionBooleanSupplier) {

		//
		// Unusual Code: actions will call this method when their 'isEnabledForContext()' is 
		//               called.  If the decompiler is still working, we return true here so
		//               the action is considered enabled.  This allows any key bindings registered
		//               for the action to get consumed.  If we did not returned false when
		//               the decompiler was still working, then the key binding would not match and
		//               the system would pass the key binding up to the global action system,
		//               which we do not want.
		//
		//               Each action that needs state from the decompiler must call this method   
		//               from 'isEnabledForContext()'.  Also, each action must call 
		//               'performAction()' on this class, which will skip the action's work and
		//               show an message if the decompiler is busy.
		//
		if (isDecompiling()) {
			return true;
		}

		return actionBooleanSupplier.get();
	}
}
