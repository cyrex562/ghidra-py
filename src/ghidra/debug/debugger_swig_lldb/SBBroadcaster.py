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

public class SBBroadcaster {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected SBBroadcaster(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(SBBroadcaster obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected static long swigRelease(SBBroadcaster obj) {
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
        lldbJNI.delete_SBBroadcaster(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public SBBroadcaster() {
    this(lldbJNI.new_SBBroadcaster__SWIG_0(), true);
  }

  public SBBroadcaster(String name) {
    this(lldbJNI.new_SBBroadcaster__SWIG_1(name), true);
  }

  public SBBroadcaster(SBBroadcaster rhs) {
    this(lldbJNI.new_SBBroadcaster__SWIG_2(SBBroadcaster.getCPtr(rhs), rhs), true);
  }

  public boolean IsValid() {
    return lldbJNI.SBBroadcaster_IsValid(swigCPtr, this);
  }

  public void Clear() {
    lldbJNI.SBBroadcaster_Clear(swigCPtr, this);
  }

  public void BroadcastEventByType(long event_type, boolean unique) {
    lldbJNI.SBBroadcaster_BroadcastEventByType__SWIG_0(swigCPtr, this, event_type, unique);
  }

  public void BroadcastEventByType(long event_type) {
    lldbJNI.SBBroadcaster_BroadcastEventByType__SWIG_1(swigCPtr, this, event_type);
  }

  public void BroadcastEvent(SBEvent event, boolean unique) {
    lldbJNI.SBBroadcaster_BroadcastEvent__SWIG_0(swigCPtr, this, SBEvent.getCPtr(event), event, unique);
  }

  public void BroadcastEvent(SBEvent event) {
    lldbJNI.SBBroadcaster_BroadcastEvent__SWIG_1(swigCPtr, this, SBEvent.getCPtr(event), event);
  }

  public void AddInitialEventsToListener(SBListener listener, long requested_events) {
    lldbJNI.SBBroadcaster_AddInitialEventsToListener(swigCPtr, this, SBListener.getCPtr(listener), listener, requested_events);
  }

  public long AddListener(SBListener listener, long event_mask) {
    return lldbJNI.SBBroadcaster_AddListener(swigCPtr, this, SBListener.getCPtr(listener), listener, event_mask);
  }

  public String GetName() {
    return lldbJNI.SBBroadcaster_GetName(swigCPtr, this);
  }

  public boolean EventTypeHasListeners(long event_type) {
    return lldbJNI.SBBroadcaster_EventTypeHasListeners(swigCPtr, this, event_type);
  }

  public boolean RemoveListener(SBListener listener, long event_mask) {
    return lldbJNI.SBBroadcaster_RemoveListener__SWIG_0(swigCPtr, this, SBListener.getCPtr(listener), listener, event_mask);
  }

  public boolean RemoveListener(SBListener listener) {
    return lldbJNI.SBBroadcaster_RemoveListener__SWIG_1(swigCPtr, this, SBListener.getCPtr(listener), listener);
  }

}
