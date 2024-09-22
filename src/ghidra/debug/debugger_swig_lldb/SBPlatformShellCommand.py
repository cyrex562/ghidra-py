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

public class SBPlatformShellCommand {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected SBPlatformShellCommand(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(SBPlatformShellCommand obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected static long swigRelease(SBPlatformShellCommand obj) {
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
        lldbJNI.delete_SBPlatformShellCommand(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public SBPlatformShellCommand(String shell, String shell_command) {
    this(lldbJNI.new_SBPlatformShellCommand__SWIG_0(shell, shell_command), true);
  }

  public SBPlatformShellCommand(String shell_command) {
    this(lldbJNI.new_SBPlatformShellCommand__SWIG_1(shell_command), true);
  }

  public SBPlatformShellCommand(SBPlatformShellCommand rhs) {
    this(lldbJNI.new_SBPlatformShellCommand__SWIG_2(SBPlatformShellCommand.getCPtr(rhs), rhs), true);
  }

  public void Clear() {
    lldbJNI.SBPlatformShellCommand_Clear(swigCPtr, this);
  }

  public String GetShell() {
    return lldbJNI.SBPlatformShellCommand_GetShell(swigCPtr, this);
  }

  public void SetShell(String shell) {
    lldbJNI.SBPlatformShellCommand_SetShell(swigCPtr, this, shell);
  }

  public String GetCommand() {
    return lldbJNI.SBPlatformShellCommand_GetCommand(swigCPtr, this);
  }

  public void SetCommand(String shell_command) {
    lldbJNI.SBPlatformShellCommand_SetCommand(swigCPtr, this, shell_command);
  }

  public String GetWorkingDirectory() {
    return lldbJNI.SBPlatformShellCommand_GetWorkingDirectory(swigCPtr, this);
  }

  public void SetWorkingDirectory(String path) {
    lldbJNI.SBPlatformShellCommand_SetWorkingDirectory(swigCPtr, this, path);
  }

  public long GetTimeoutSeconds() {
    return lldbJNI.SBPlatformShellCommand_GetTimeoutSeconds(swigCPtr, this);
  }

  public void SetTimeoutSeconds(long sec) {
    lldbJNI.SBPlatformShellCommand_SetTimeoutSeconds(swigCPtr, this, sec);
  }

  public int GetSignal() {
    return lldbJNI.SBPlatformShellCommand_GetSignal(swigCPtr, this);
  }

  public int GetStatus() {
    return lldbJNI.SBPlatformShellCommand_GetStatus(swigCPtr, this);
  }

  public String GetOutput() {
    return lldbJNI.SBPlatformShellCommand_GetOutput(swigCPtr, this);
  }

}
