# /* ###
 * IP: Apache License 2.0 with LLVM Exceptions
 */
# /* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (https://www.swig.org).
 * Version 4.1.1
 *
 * Do not make changes to this file unless you know what you are doing - modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package SWIG;

public class SBCommandInterpreter {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected SBCommandInterpreter(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(SBCommandInterpreter obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected static long swigRelease(SBCommandInterpreter obj) {
    long ptr = 0;
    if (obj != null) {
      if (!obj.swigCMemOwn)
        throw new RuntimeException("Cannot release ownership as memory is not owned");
      ptr = obj.swigCPtr;
      obj.swigCMemOwn = false;
      obj.delete();
    }
    return ptr;
  }

  @SuppressWarnings("deprecation")
  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        lldbJNI.delete_SBCommandInterpreter(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public SBCommandInterpreter(SBCommandInterpreter rhs) {
    this(lldbJNI.new_SBCommandInterpreter(SBCommandInterpreter.getCPtr(rhs), rhs), true);
  }

  public static String GetArgumentTypeAsCString(CommandArgumentType arg_type) {
    return lldbJNI.SBCommandInterpreter_GetArgumentTypeAsCString(arg_type.swigValue());
  }

  public static String GetArgumentDescriptionAsCString(CommandArgumentType arg_type) {
    return lldbJNI.SBCommandInterpreter_GetArgumentDescriptionAsCString(arg_type.swigValue());
  }

  public static boolean EventIsCommandInterpreterEvent(SBEvent event) {
    return lldbJNI.SBCommandInterpreter_EventIsCommandInterpreterEvent(SBEvent.getCPtr(event), event);
  }

  public boolean IsValid() {
    return lldbJNI.SBCommandInterpreter_IsValid(swigCPtr, this);
  }

  public boolean CommandExists(String cmd) {
    return lldbJNI.SBCommandInterpreter_CommandExists(swigCPtr, this, cmd);
  }

  public boolean UserCommandExists(String cmd) {
    return lldbJNI.SBCommandInterpreter_UserCommandExists(swigCPtr, this, cmd);
  }

  public boolean AliasExists(String cmd) {
    return lldbJNI.SBCommandInterpreter_AliasExists(swigCPtr, this, cmd);
  }

  public SBBroadcaster GetBroadcaster() {
    return new SBBroadcaster(lldbJNI.SBCommandInterpreter_GetBroadcaster(swigCPtr, this), true);
  }

  public static String GetBroadcasterClass() {
    return lldbJNI.SBCommandInterpreter_GetBroadcasterClass();
  }

  public boolean HasCommands() {
    return lldbJNI.SBCommandInterpreter_HasCommands(swigCPtr, this);
  }

  public boolean HasAliases() {
    return lldbJNI.SBCommandInterpreter_HasAliases(swigCPtr, this);
  }

  public boolean HasAliasOptions() {
    return lldbJNI.SBCommandInterpreter_HasAliasOptions(swigCPtr, this);
  }

  public boolean IsInteractive() {
    return lldbJNI.SBCommandInterpreter_IsInteractive(swigCPtr, this);
  }

  public SBProcess GetProcess() {
    return new SBProcess(lldbJNI.SBCommandInterpreter_GetProcess(swigCPtr, this), true);
  }

  public SBDebugger GetDebugger() {
    return new SBDebugger(lldbJNI.SBCommandInterpreter_GetDebugger(swigCPtr, this), true);
  }

  public void SourceInitFileInHomeDirectory(SBCommandReturnObject result) {
    lldbJNI.SBCommandInterpreter_SourceInitFileInHomeDirectory__SWIG_0(swigCPtr, this, SBCommandReturnObject.getCPtr(result), result);
  }

  public void SourceInitFileInHomeDirectory(SBCommandReturnObject result, boolean is_repl) {
    lldbJNI.SBCommandInterpreter_SourceInitFileInHomeDirectory__SWIG_1(swigCPtr, this, SBCommandReturnObject.getCPtr(result), result, is_repl);
  }

  public void SourceInitFileInCurrentWorkingDirectory(SBCommandReturnObject result) {
    lldbJNI.SBCommandInterpreter_SourceInitFileInCurrentWorkingDirectory(swigCPtr, this, SBCommandReturnObject.getCPtr(result), result);
  }

  public ReturnStatus HandleCommand(String command_line, SBCommandReturnObject result, boolean add_to_history) {
    return ReturnStatus.swigToEnum(lldbJNI.SBCommandInterpreter_HandleCommand__SWIG_0(swigCPtr, this, command_line, SBCommandReturnObject.getCPtr(result), result, add_to_history));
  }

  public ReturnStatus HandleCommand(String command_line, SBCommandReturnObject result) {
    return ReturnStatus.swigToEnum(lldbJNI.SBCommandInterpreter_HandleCommand__SWIG_1(swigCPtr, this, command_line, SBCommandReturnObject.getCPtr(result), result));
  }

  public ReturnStatus HandleCommand(String command_line, SBExecutionContext exe_ctx, SBCommandReturnObject result, boolean add_to_history) {
    return ReturnStatus.swigToEnum(lldbJNI.SBCommandInterpreter_HandleCommand__SWIG_2(swigCPtr, this, command_line, SBExecutionContext.getCPtr(exe_ctx), exe_ctx, SBCommandReturnObject.getCPtr(result), result, add_to_history));
  }

  public ReturnStatus HandleCommand(String command_line, SBExecutionContext exe_ctx, SBCommandReturnObject result) {
    return ReturnStatus.swigToEnum(lldbJNI.SBCommandInterpreter_HandleCommand__SWIG_3(swigCPtr, this, command_line, SBExecutionContext.getCPtr(exe_ctx), exe_ctx, SBCommandReturnObject.getCPtr(result), result));
  }

  public void HandleCommandsFromFile(SBFileSpec file, SBExecutionContext override_context, SBCommandInterpreterRunOptions options, SBCommandReturnObject result) {
    lldbJNI.SBCommandInterpreter_HandleCommandsFromFile(swigCPtr, this, SBFileSpec.getCPtr(file), file, SBExecutionContext.getCPtr(override_context), override_context, SBCommandInterpreterRunOptions.getCPtr(options), options, SBCommandReturnObject.getCPtr(result), result);
  }

  public int HandleCompletion(String current_line, long cursor_pos, int match_start_point, int max_return_elements, SBStringList matches) {
    return lldbJNI.SBCommandInterpreter_HandleCompletion(swigCPtr, this, current_line, cursor_pos, match_start_point, max_return_elements, SBStringList.getCPtr(matches), matches);
  }

  public int HandleCompletionWithDescriptions(String current_line, long cursor_pos, int match_start_point, int max_return_elements, SBStringList matches, SBStringList descriptions) {
    return lldbJNI.SBCommandInterpreter_HandleCompletionWithDescriptions(swigCPtr, this, current_line, cursor_pos, match_start_point, max_return_elements, SBStringList.getCPtr(matches), matches, SBStringList.getCPtr(descriptions), descriptions);
  }

  public boolean WasInterrupted() {
    return lldbJNI.SBCommandInterpreter_WasInterrupted(swigCPtr, this);
  }

  public boolean InterruptCommand() {
    return lldbJNI.SBCommandInterpreter_InterruptCommand(swigCPtr, this);
  }

  public boolean IsActive() {
    return lldbJNI.SBCommandInterpreter_IsActive(swigCPtr, this);
  }

  public String GetIOHandlerControlSequence(char ch) {
    return lldbJNI.SBCommandInterpreter_GetIOHandlerControlSequence(swigCPtr, this, ch);
  }

  public boolean GetPromptOnQuit() {
    return lldbJNI.SBCommandInterpreter_GetPromptOnQuit(swigCPtr, this);
  }

  public void SetPromptOnQuit(boolean b) {
    lldbJNI.SBCommandInterpreter_SetPromptOnQuit(swigCPtr, this, b);
  }

  public void AllowExitCodeOnQuit(boolean allow) {
    lldbJNI.SBCommandInterpreter_AllowExitCodeOnQuit(swigCPtr, this, allow);
  }

  public boolean HasCustomQuitExitCode() {
    return lldbJNI.SBCommandInterpreter_HasCustomQuitExitCode(swigCPtr, this);
  }

  public int GetQuitStatus() {
    return lldbJNI.SBCommandInterpreter_GetQuitStatus(swigCPtr, this);
  }

  public void ResolveCommand(String command_line, SBCommandReturnObject result) {
    lldbJNI.SBCommandInterpreter_ResolveCommand(swigCPtr, this, command_line, SBCommandReturnObject.getCPtr(result), result);
  }

  public final static int eBroadcastBitThreadShouldExit = lldbJNI.SBCommandInterpreter_eBroadcastBitThreadShouldExit_get();
  public final static int eBroadcastBitResetPrompt = lldbJNI.SBCommandInterpreter_eBroadcastBitResetPrompt_get();
  public final static int eBroadcastBitQuitCommandReceived = lldbJNI.SBCommandInterpreter_eBroadcastBitQuitCommandReceived_get();
  public final static int eBroadcastBitAsynchronousOutputData = lldbJNI.SBCommandInterpreter_eBroadcastBitAsynchronousOutputData_get();
  public final static int eBroadcastBitAsynchronousErrorData = lldbJNI.SBCommandInterpreter_eBroadcastBitAsynchronousErrorData_get();

}
