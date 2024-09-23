# /* ###
#  * IP: GHIDRA
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  * 
#  *      http://www.apache.org/licenses/LICENSE-2.0
#  * 
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#  */
# package db;



# import db.buffers.DataBuffer;
from typing import Self


from .buffer import Buffer
from .data_buffer import DataBuffer
from .primitive_field import PrimitiveField
from .field import Field

# /**
#  * <code>BooleanField</code> provides a wrapper for boolean data which is read or
#  * written to a Record. 
#  */
# public final class BooleanField extends PrimitiveField {
class BooleanField(PrimitiveField):

    # /**
    #  * Minimum boolean field value (FALSE)
    #  */
    # public static final BooleanField MIN_VALUE = new BooleanField(false, true);
    # MIN_VALUE = Self(False, True)
    @classmethod
    def MIN_VALUE(cls) -> Self:
        return cls(False, True)

    # /**
    #  * Maximum boolean field value (TRUE)
    #  */
    # public static final BooleanField MAX_VALUE = new BooleanField(true, true);
    # MAX_VALUE = Self(True, True)
    @classmethod
    def MAX_VALUE(cls) -> Self:
        return cls(True, True)
    
    # /**
    #  * Instance intended for defining a {@link Table} {@link Schema}
    #  */
    # public static final BooleanField INSTANCE = MIN_VALUE;
    INSTANCE: Self|None = None
    # INSTANCE = MIN_VALUE(Self)

    # private byte value;

    # /**
    #  * Construct a boolean data field with an initial value of false.
    #  */
    # public BooleanField() {
    # }
    def __init__(self, b: bool | None = None, immutable: bool | None = None):
        self.value = 0
        super().__init__()
        if b is not None:
            self.value = 1 if b else 0
        if immutable is not None:
            self.immutable = immutable
            
        

    # /**
    #  * Construct a boolean data field with an initial value of b.
    #  * @param b initial value
    #  */
    # public BooleanField(boolean b) {
    #     this(b, false);
    # }

    # @Override
    # void setNull() {
    #     super.setNull();
    #     value = 0;
    # }
    def setNull(self) -> None:
        super().setNull()
        self.value = 0

    # /**
    #  * Construct a boolean data field with an initial value of b.
    #  * @param b initial value
    #  * @param immutable true if field value is immutable
    #  */
    # BooleanField(boolean b, boolean immutable) {
    #     super(immutable);
    #     value = b ? (byte) 1 : (byte) 0;
    # }

    # @Override
    # public boolean getBooleanValue() {
    #     return (value == 0) ? false : true;
    # }
    def getBooleanValue(self)    -> bool:
        return self.value != 0

    # @Override
    # public void setBooleanValue(boolean b) {
    #     updatingPrimitiveValue();
    #     this.value = b ? (byte) 1 : (byte) 0;
    # }
    def setBooleanValue(self, value: bool):
        self.updatingPrimitiveValue()
        self.value = 1 if value else 0

    # @Override
    # int length() {
    #     return 1;
    # }
    def length(self) -> int:
        return 1

    # @Override
    # int write(Buffer buf, int offset) throws IndexOutOfBoundsException, IOException {
    #     return buf.putByte(offset, value);
    # }
    def write(self, buf: Buffer, offset: int) -> int:
        return buf.putByte(offset, self.value)

    # @Override
    # int read(Buffer buf, int offset) throws IndexOutOfBoundsException, IOException {
    #     updatingPrimitiveValue();
    #     value = buf.getByte(offset);
    #     return offset + 1;
    # }
    def read(self, buf: Buffer, offset: int) -> int:
        self.updatingPrimitiveValue()
        self.value = buf.getByte(offset)
        return offset + 1

    # @Override
    # int readLength(Buffer buf, int offset) {
    #     return 1;
    # }
    def readLength(self, buf: Buffer, offset: int) -> int:
        return 1

    # @Override
    # byte getFieldType() {
    #     return BOOLEAN_TYPE;
    # }
    def getFieldType(self):
        return super().getFieldType()

    # @Override
    # public String getValueAsString() {
    #     return Boolean.toString(getBooleanValue());
    # }
    def getValueAsString(self) -> str:
        return super().getValueAsString()

    # @Override
    # public boolean equals(Object obj) {
    #     if (!(obj instanceof BooleanField)) {
    #         return false;
    #     }
    #     return ((BooleanField) obj).value == value;
    # }
    def equals(self, obj: object) -> bool:
        if not isinstance(obj, BooleanField):
            return False
        return obj.value == self.value

    # @Override
    # public int compareTo(Field o) {
    #     BooleanField f = (BooleanField) o;
    #     if (value == f.value) {
    #         return 0;
    #     }
    #     else if (value < f.value) {
    #         return -1;
    #     }
    #     return 1;
    # }
    def compareTo(self, o: Field) -> int:
        f = o
        if self.value == f.value:
            return 0
        elif self.value < f.value:
            return -1
        return 1

    # @Override
    # int compareTo(DataBuffer buffer, int offset) {
    #     byte otherValue = buffer.getByte(offset);
    #     if (value == otherValue) {
    #         return 0;
    #     }
    #     else if (value < otherValue) {
    #         return -1;
    #     }
    #     return 1;
    # }
    def compare_to_databuffer(self, buffer: DataBuffer, offset: int) -> int:
        otherValue = buffer.getByte(offset)
        if self.value == otherValue:
            return 0
        elif self.value < otherValue:
            return -1
        return 1

    # @Override
    # public BooleanField copyField() {
    #     if (isNull()) {
    #         BooleanField copy = new BooleanField();
    #         copy.setNull();
    #         return copy;
    #     }
    #     return new BooleanField(getLongValue() != 0);
    # }
    def copyField(self) -> Self:
        if self.isNull():
            copy = BooleanField()
            copy.setNull()
            return copy
        return BooleanField(self.getLongValue() != 0)

    # @Override
    # public BooleanField newField() {
    #     return new BooleanField();
    # }
    def newField(self) -> Self:
        return BooleanField()

    # @Override
    # public long getLongValue() {
    #     return value;
    # }
    def getLongValue(self) -> int:
        return self.value

    # @Override
    # public byte[] getBinaryData() {
    #     return new byte[] { value };
    # }
    def getBinaryData(self):
        return [self.value]

    # @Override
    # public void setBinaryData(byte[] bytes) {
    #     if (bytes == null) {
    #         setNull();
    #         return;
    #     }
    #     if (bytes.length != 1) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     updatingPrimitiveValue();
    #     value = bytes[0];
    # }
    def setBinaryData(self, bytes):
        if bytes is None:
            self.setNull()
            return
        if len(bytes) != 1:
            raise IllegalFieldAccessException()
        self.updatingPrimitiveValue()
        self.value = bytes[0]

    # @Override
    # public int hashCode() {
    #     return value;
    # }
    def hashCode(self) -> int:
        return self.value

    # @Override
    # BooleanField getMinValue() {
    #     return MIN_VALUE;
    # }
    def getMinValue(self) -> Self:
        return BooleanField.MIN_VALUE()

    # @Override
    # BooleanField getMaxValue() {
    #     return MAX_VALUE;
    # }
    def getMaxValue(self) -> Self:
        return BooleanField.MAX_VALUE()

# }

BooleanField.INSTANCE = BooleanField.MIN_VALUE()