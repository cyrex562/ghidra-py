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

public class SBModule {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected SBModule(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(SBModule obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected static long swigRelease(SBModule obj) {
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
        lldbJNI.delete_SBModule(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public SBModule() {
    this(lldbJNI.new_SBModule__SWIG_0(), true);
  }

  public SBModule(SBModule rhs) {
    this(lldbJNI.new_SBModule__SWIG_1(SBModule.getCPtr(rhs), rhs), true);
  }

  public SBModule(SBModuleSpec module_spec) {
    this(lldbJNI.new_SBModule__SWIG_2(SBModuleSpec.getCPtr(module_spec), module_spec), true);
  }

  public SBModule(SBProcess process, java.math.BigInteger header_addr) {
    this(lldbJNI.new_SBModule__SWIG_3(SBProcess.getCPtr(process), process, header_addr), true);
  }

  public boolean IsValid() {
    return lldbJNI.SBModule_IsValid(swigCPtr, this);
  }

  public void Clear() {
    lldbJNI.SBModule_Clear(swigCPtr, this);
  }

  public boolean IsFileBacked() {
    return lldbJNI.SBModule_IsFileBacked(swigCPtr, this);
  }

  public SBFileSpec GetFileSpec() {
    return new SBFileSpec(lldbJNI.SBModule_GetFileSpec(swigCPtr, this), true);
  }

  public SBFileSpec GetPlatformFileSpec() {
    return new SBFileSpec(lldbJNI.SBModule_GetPlatformFileSpec(swigCPtr, this), true);
  }

  public boolean SetPlatformFileSpec(SBFileSpec platform_file) {
    return lldbJNI.SBModule_SetPlatformFileSpec(swigCPtr, this, SBFileSpec.getCPtr(platform_file), platform_file);
  }

  public SBFileSpec GetRemoteInstallFileSpec() {
    return new SBFileSpec(lldbJNI.SBModule_GetRemoteInstallFileSpec(swigCPtr, this), true);
  }

  public boolean SetRemoteInstallFileSpec(SBFileSpec file) {
    return lldbJNI.SBModule_SetRemoteInstallFileSpec(swigCPtr, this, SBFileSpec.getCPtr(file), file);
  }

  public ByteOrder GetByteOrder() {
    return ByteOrder.swigToEnum(lldbJNI.SBModule_GetByteOrder(swigCPtr, this));
  }

  public long GetAddressByteSize() {
    return lldbJNI.SBModule_GetAddressByteSize(swigCPtr, this);
  }

  public String GetTriple() {
    return lldbJNI.SBModule_GetTriple(swigCPtr, this);
  }

  public SWIGTYPE_p_unsigned_char GetUUIDBytes() {
    long cPtr = lldbJNI.SBModule_GetUUIDBytes(swigCPtr, this);
    return (cPtr == 0) ? null : new SWIGTYPE_p_unsigned_char(cPtr, false);
  }

  public String GetUUIDString() {
    return lldbJNI.SBModule_GetUUIDString(swigCPtr, this);
  }

  public SBSection FindSection(String sect_name) {
    return new SBSection(lldbJNI.SBModule_FindSection(swigCPtr, this, sect_name), true);
  }

  public SBAddress ResolveFileAddress(java.math.BigInteger vm_addr) {
    return new SBAddress(lldbJNI.SBModule_ResolveFileAddress(swigCPtr, this, vm_addr), true);
  }

  public SBSymbolContext ResolveSymbolContextForAddress(SBAddress addr, long resolve_scope) {
    return new SBSymbolContext(lldbJNI.SBModule_ResolveSymbolContextForAddress(swigCPtr, this, SBAddress.getCPtr(addr), addr, resolve_scope), true);
  }

  public boolean GetDescription(SBStream description) {
    return lldbJNI.SBModule_GetDescription(swigCPtr, this, SBStream.getCPtr(description), description);
  }

  public long GetNumCompileUnits() {
    return lldbJNI.SBModule_GetNumCompileUnits(swigCPtr, this);
  }

  public SBCompileUnit GetCompileUnitAtIndex(long arg0) {
    return new SBCompileUnit(lldbJNI.SBModule_GetCompileUnitAtIndex(swigCPtr, this, arg0), true);
  }

  public SBSymbolContextList FindCompileUnits(SBFileSpec sb_file_spec) {
    return new SBSymbolContextList(lldbJNI.SBModule_FindCompileUnits(swigCPtr, this, SBFileSpec.getCPtr(sb_file_spec), sb_file_spec), true);
  }

  public long GetNumSymbols() {
    return lldbJNI.SBModule_GetNumSymbols(swigCPtr, this);
  }

  public SBSymbol GetSymbolAtIndex(long idx) {
    return new SBSymbol(lldbJNI.SBModule_GetSymbolAtIndex(swigCPtr, this, idx), true);
  }

  public SBSymbol FindSymbol(String name, SymbolType type) {
    return new SBSymbol(lldbJNI.SBModule_FindSymbol__SWIG_0(swigCPtr, this, name, type.swigValue()), true);
  }

  public SBSymbol FindSymbol(String name) {
    return new SBSymbol(lldbJNI.SBModule_FindSymbol__SWIG_1(swigCPtr, this, name), true);
  }

  public SBSymbolContextList FindSymbols(String name, SymbolType type) {
    return new SBSymbolContextList(lldbJNI.SBModule_FindSymbols__SWIG_0(swigCPtr, this, name, type.swigValue()), true);
  }

  public SBSymbolContextList FindSymbols(String name) {
    return new SBSymbolContextList(lldbJNI.SBModule_FindSymbols__SWIG_1(swigCPtr, this, name), true);
  }

  public long GetNumSections() {
    return lldbJNI.SBModule_GetNumSections(swigCPtr, this);
  }

  public SBSection GetSectionAtIndex(long idx) {
    return new SBSection(lldbJNI.SBModule_GetSectionAtIndex(swigCPtr, this, idx), true);
  }

  public SBSymbolContextList FindFunctions(String name, long name_type_mask) {
    return new SBSymbolContextList(lldbJNI.SBModule_FindFunctions__SWIG_0(swigCPtr, this, name, name_type_mask), true);
  }

  public SBSymbolContextList FindFunctions(String name) {
    return new SBSymbolContextList(lldbJNI.SBModule_FindFunctions__SWIG_1(swigCPtr, this, name), true);
  }

  public SBValueList FindGlobalVariables(SBTarget target, String name, long max_matches) {
    return new SBValueList(lldbJNI.SBModule_FindGlobalVariables(swigCPtr, this, SBTarget.getCPtr(target), target, name, max_matches), true);
  }

  public SBValue FindFirstGlobalVariable(SBTarget target, String name) {
    return new SBValue(lldbJNI.SBModule_FindFirstGlobalVariable(swigCPtr, this, SBTarget.getCPtr(target), target, name), true);
  }

  public SBType FindFirstType(String name) {
    return new SBType(lldbJNI.SBModule_FindFirstType(swigCPtr, this, name), true);
  }

  public SBTypeList FindTypes(String type) {
    return new SBTypeList(lldbJNI.SBModule_FindTypes(swigCPtr, this, type), true);
  }

  public SBType GetTypeByID(java.math.BigInteger uid) {
    return new SBType(lldbJNI.SBModule_GetTypeByID(swigCPtr, this, uid), true);
  }

  public SBType GetBasicType(BasicType type) {
    return new SBType(lldbJNI.SBModule_GetBasicType(swigCPtr, this, type.swigValue()), true);
  }

  public SBTypeList GetTypes(long type_mask) {
    return new SBTypeList(lldbJNI.SBModule_GetTypes__SWIG_0(swigCPtr, this, type_mask), true);
  }

  public SBTypeList GetTypes() {
    return new SBTypeList(lldbJNI.SBModule_GetTypes__SWIG_1(swigCPtr, this), true);
  }

  public long GetVersion(SWIGTYPE_p_unsigned_int versions, long num_versions) {
    return lldbJNI.SBModule_GetVersion(swigCPtr, this, SWIGTYPE_p_unsigned_int.getCPtr(versions), num_versions);
  }

  public SBFileSpec GetSymbolFileSpec() {
    return new SBFileSpec(lldbJNI.SBModule_GetSymbolFileSpec(swigCPtr, this), true);
  }

  public SBAddress GetObjectFileHeaderAddress() {
    return new SBAddress(lldbJNI.SBModule_GetObjectFileHeaderAddress(swigCPtr, this), true);
  }

  public SBAddress GetObjectFileEntryPointAddress() {
    return new SBAddress(lldbJNI.SBModule_GetObjectFileEntryPointAddress(swigCPtr, this), true);
  }

  public static long GetNumberAllocatedModules() {
    return lldbJNI.SBModule_GetNumberAllocatedModules();
  }

  public static void GarbageCollectAllocatedModules() {
    lldbJNI.SBModule_GarbageCollectAllocatedModules();
  }

  public String __repr__() {
    return lldbJNI.SBModule___repr__(swigCPtr, this);
  }

}
