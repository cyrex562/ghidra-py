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

public class SBThreadCollection {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected SBThreadCollection(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(SBThreadCollection obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected static long swigRelease(SBThreadCollection obj) {
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
        lldbJNI.delete_SBThreadCollection(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public SBThreadCollection() {
    this(lldbJNI.new_SBThreadCollection__SWIG_0(), true);
  }

  public SBThreadCollection(SBThreadCollection rhs) {
    this(lldbJNI.new_SBThreadCollection__SWIG_1(SBThreadCollection.getCPtr(rhs), rhs), true);
  }

  public boolean IsValid() {
    return lldbJNI.SBThreadCollection_IsValid(swigCPtr, this);
  }

  public long GetSize() {
    return lldbJNI.SBThreadCollection_GetSize(swigCPtr, this);
  }

  public SBThread GetThreadAtIndex(long idx) {
    return new SBThread(lldbJNI.SBThreadCollection_GetThreadAtIndex(swigCPtr, this, idx), true);
  }

}
