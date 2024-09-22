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

public final class QueueKind {
  public final static QueueKind eQueueKindUnknown = new QueueKind("eQueueKindUnknown", lldbJNI.eQueueKindUnknown_get());
  public final static QueueKind eQueueKindSerial = new QueueKind("eQueueKindSerial");
  public final static QueueKind eQueueKindConcurrent = new QueueKind("eQueueKindConcurrent");

  public final int swigValue() {
    return swigValue;
  }

  public String toString() {
    return swigName;
  }

  public static QueueKind swigToEnum(int swigValue) {
    if (swigValue < swigValues.length && swigValue >= 0 && swigValues[swigValue].swigValue == swigValue)
      return swigValues[swigValue];
    for (int i = 0; i < swigValues.length; i++)
      if (swigValues[i].swigValue == swigValue)
        return swigValues[i];
    throw new IllegalArgumentException("No enum " + QueueKind.class + " with value " + swigValue);
  }

  private QueueKind(String swigName) {
    this.swigName = swigName;
    this.swigValue = swigNext++;
  }

  private QueueKind(String swigName, int swigValue) {
    this.swigName = swigName;
    this.swigValue = swigValue;
    swigNext = swigValue+1;
  }

  private QueueKind(String swigName, QueueKind swigEnum) {
    this.swigName = swigName;
    this.swigValue = swigEnum.swigValue;
    swigNext = this.swigValue+1;
  }

  private static QueueKind[] swigValues = { eQueueKindUnknown, eQueueKindSerial, eQueueKindConcurrent };
  private static int swigNext = 0;
  private final int swigValue;
  private final String swigName;
}

