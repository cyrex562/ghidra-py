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

public class SBTypeSummary {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected SBTypeSummary(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(SBTypeSummary obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected static long swigRelease(SBTypeSummary obj) {
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
        lldbJNI.delete_SBTypeSummary(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public SBTypeSummary() {
    this(lldbJNI.new_SBTypeSummary__SWIG_0(), true);
  }

  public static SBTypeSummary CreateWithSummaryString(String data, long options) {
    return new SBTypeSummary(lldbJNI.SBTypeSummary_CreateWithSummaryString__SWIG_0(data, options), true);
  }

  public static SBTypeSummary CreateWithSummaryString(String data) {
    return new SBTypeSummary(lldbJNI.SBTypeSummary_CreateWithSummaryString__SWIG_1(data), true);
  }

  public static SBTypeSummary CreateWithFunctionName(String data, long options) {
    return new SBTypeSummary(lldbJNI.SBTypeSummary_CreateWithFunctionName__SWIG_0(data, options), true);
  }

  public static SBTypeSummary CreateWithFunctionName(String data) {
    return new SBTypeSummary(lldbJNI.SBTypeSummary_CreateWithFunctionName__SWIG_1(data), true);
  }

  public static SBTypeSummary CreateWithScriptCode(String data, long options) {
    return new SBTypeSummary(lldbJNI.SBTypeSummary_CreateWithScriptCode__SWIG_0(data, options), true);
  }

  public static SBTypeSummary CreateWithScriptCode(String data) {
    return new SBTypeSummary(lldbJNI.SBTypeSummary_CreateWithScriptCode__SWIG_1(data), true);
  }

  public SBTypeSummary(SBTypeSummary rhs) {
    this(lldbJNI.new_SBTypeSummary__SWIG_1(SBTypeSummary.getCPtr(rhs), rhs), true);
  }

  public boolean IsValid() {
    return lldbJNI.SBTypeSummary_IsValid(swigCPtr, this);
  }

  public boolean IsFunctionCode() {
    return lldbJNI.SBTypeSummary_IsFunctionCode(swigCPtr, this);
  }

  public boolean IsFunctionName() {
    return lldbJNI.SBTypeSummary_IsFunctionName(swigCPtr, this);
  }

  public boolean IsSummaryString() {
    return lldbJNI.SBTypeSummary_IsSummaryString(swigCPtr, this);
  }

  public String GetData() {
    return lldbJNI.SBTypeSummary_GetData(swigCPtr, this);
  }

  public void SetSummaryString(String data) {
    lldbJNI.SBTypeSummary_SetSummaryString(swigCPtr, this, data);
  }

  public void SetFunctionName(String data) {
    lldbJNI.SBTypeSummary_SetFunctionName(swigCPtr, this, data);
  }

  public void SetFunctionCode(String data) {
    lldbJNI.SBTypeSummary_SetFunctionCode(swigCPtr, this, data);
  }

  public long GetOptions() {
    return lldbJNI.SBTypeSummary_GetOptions(swigCPtr, this);
  }

  public void SetOptions(long arg0) {
    lldbJNI.SBTypeSummary_SetOptions(swigCPtr, this, arg0);
  }

  public boolean GetDescription(SBStream description, DescriptionLevel description_level) {
    return lldbJNI.SBTypeSummary_GetDescription(swigCPtr, this, SBStream.getCPtr(description), description, description_level.swigValue());
  }

  public boolean DoesPrintValue(SBValue value) {
    return lldbJNI.SBTypeSummary_DoesPrintValue(swigCPtr, this, SBValue.getCPtr(value), value);
  }

  public boolean IsEqualTo(SBTypeSummary rhs) {
    return lldbJNI.SBTypeSummary_IsEqualTo(swigCPtr, this, SBTypeSummary.getCPtr(rhs), rhs);
  }

  public String __repr__() {
    return lldbJNI.SBTypeSummary___repr__(swigCPtr, this);
  }

}
