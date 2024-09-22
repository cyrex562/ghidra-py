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

public class SBSymbol {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected SBSymbol(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(SBSymbol obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected static long swigRelease(SBSymbol obj) {
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
        lldbJNI.delete_SBSymbol(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public SBSymbol() {
    this(lldbJNI.new_SBSymbol__SWIG_0(), true);
  }

  public SBSymbol(SBSymbol rhs) {
    this(lldbJNI.new_SBSymbol__SWIG_1(SBSymbol.getCPtr(rhs), rhs), true);
  }

  public boolean IsValid() {
    return lldbJNI.SBSymbol_IsValid(swigCPtr, this);
  }

  public String GetName() {
    return lldbJNI.SBSymbol_GetName(swigCPtr, this);
  }

  public String GetDisplayName() {
    return lldbJNI.SBSymbol_GetDisplayName(swigCPtr, this);
  }

  public String GetMangledName() {
    return lldbJNI.SBSymbol_GetMangledName(swigCPtr, this);
  }

  public SBInstructionList GetInstructions(SBTarget target) {
    return new SBInstructionList(lldbJNI.SBSymbol_GetInstructions__SWIG_0(swigCPtr, this, SBTarget.getCPtr(target), target), true);
  }

  public SBInstructionList GetInstructions(SBTarget target, String flavor_string) {
    return new SBInstructionList(lldbJNI.SBSymbol_GetInstructions__SWIG_1(swigCPtr, this, SBTarget.getCPtr(target), target, flavor_string), true);
  }

  public SBAddress GetStartAddress() {
    return new SBAddress(lldbJNI.SBSymbol_GetStartAddress(swigCPtr, this), true);
  }

  public SBAddress GetEndAddress() {
    return new SBAddress(lldbJNI.SBSymbol_GetEndAddress(swigCPtr, this), true);
  }

  public java.math.BigInteger GetValue() {
    return lldbJNI.SBSymbol_GetValue(swigCPtr, this);
  }

  public java.math.BigInteger GetSize() {
    return lldbJNI.SBSymbol_GetSize(swigCPtr, this);
  }

  public long GetPrologueByteSize() {
    return lldbJNI.SBSymbol_GetPrologueByteSize(swigCPtr, this);
  }

  public SymbolType GetType() {
    return SymbolType.swigToEnum(lldbJNI.SBSymbol_GetType(swigCPtr, this));
  }

  public boolean GetDescription(SBStream description) {
    return lldbJNI.SBSymbol_GetDescription(swigCPtr, this, SBStream.getCPtr(description), description);
  }

  public boolean IsExternal() {
    return lldbJNI.SBSymbol_IsExternal(swigCPtr, this);
  }

  public boolean IsSynthetic() {
    return lldbJNI.SBSymbol_IsSynthetic(swigCPtr, this);
  }

  public String __repr__() {
    return lldbJNI.SBSymbol___repr__(swigCPtr, this);
  }

}
