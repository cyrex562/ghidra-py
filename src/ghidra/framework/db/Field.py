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


from abc import ABC, abstractmethod
from typing import Optional, Self
# import db.buffers.DataBuffer;
from .data_buffer import DataBuffer


# /**
#  * <p><code>Field</code> is an abstract data wrapper for use with Records.
#  * Note that when comparing two Field instances both must be of the same 
#  * class.</p>
#  * 
#  * <p>Fields may take on a null state.  In the case of {@link FixedField}
#  * and {@link PrimitiveField} this state is distinct from value and only
#  * applies when used for a sparse column within a {@link SparseRecord}.
#  * In this sparse column situation the {@link SparseRecord#setField(int, Field)} 
#  * method may be passed a null Field argument.  Sparse columns with a 
#  * null value/state will not be indexed within a {@link Table}.
#  * 
#  * <p>Stored Schema Field Type Encoding:</p>
#  * 
#  * <p><U>8-bit Legacy Field Type Encoding (I....FFF)</U></p>
#  * Supported encodings: 0x00..0x06 and 0x80..0x86,
#  * where:
#  * <pre>
#  *     FFF  - indexed field type (0..6)
#  *     I    - index field indicator (only long primary keys were supported)
#  * </pre>
#  *   
#  * <p><U>8-bit Field Type Encoding (PPPPFFFF)</U></p>
#  * (Reserved for future field extensions: 0x88 and 0xf0..0xff)
#  * <pre>
#  *     0xff - see {@link Schema#FIELD_EXTENSION_INDICATOR}
#  * </pre>
#  * where:
#  * <pre>
#  *     FFFF - normal/indexed field type
#  *     PPPP - indexed table primary key type (1000b: LegacyIndexField)  
#  * </pre> 
#  */
# public abstract class Field implements Comparable<Field> {
class Field(ABC):
    # /**
    #  * Field type for ByteField
    #  * @see db.ByteField
    #  */
    BYTE_TYPE = 0

    # /**
    #  * Field type for ShortField
    #  * @see db.ShortField
    #  */
    SHORT_TYPE = 1

    # /**
    #  * Field type for IntField
    #  * @see db.IntField
    #  */
    INT_TYPE = 2

    # /**
    #  * Field type for LongField
    #  * @see db.LongField
    #  */
    LONG_TYPE = 3

    # /**
    #  * Field type for StringField
    #  * @see db.StringField
    #  */
    STRING_TYPE = 4

    # /**
    #  * Field type for BinaryField
    #  * @see db.BinaryField
    #  */
    BINARY_OBJ_TYPE = 5

    # /**
    #  * Field type for BooleanField
    #  * @see db.BooleanField
    #  */
    BOOLEAN_TYPE = 6

    # /**
    #  * Field type for 10-byte binary FixedField(10)
    #  * @see db.FixedField
    #  */
    FIXED_10_TYPE = 7

    # /**
    #  * Legacy Index Primary Key Field type for LongField
    #  * which was previously a boolean indicator for an index 
    #  * field with assumed long primary key.  Applies only 
    #  * to upper-nibble.  This value in the lower-nibble
    #  * is reserved for use in the special-purpose byte value 0x88.
    #  * (see {@link LegacyIndexField})
    #  */
    LEGACY_INDEX_LONG_TYPE = 8

    # // Available field types (6): 0x9..0xE

    # /**
    #  * Reserved field encoding.  Intended for special purpose 
    #  * schema used (e.g.
    #  */
    FIELD_RESERVED_15_TYPE = 0xf

    # /**
    #  * Field base type mask
    #  */
    FIELD_TYPE_MASK = 0x0F

    # /**
    #  * Field index primary key type mask
    #  */

    # public static final Field[] EMPTY_ARRAY = new Field[0];
    # TODO: Implement EMPTY_ARRAY
 
    # /**
    #  * Field type for ByteField
    #  * @see db.ByteField
    #  */
    # static final byte BYTE_TYPE = 0;

    # /**
    #  * Field type for ShortField
    #  * @see db.ShortField
    #  */
    # static final byte SHORT_TYPE = 1;

    # /**
    #  * Field type for IntField
    #  * @see db.IntField
    #  */
    # static final byte INT_TYPE = 2;

    # /**
    #  * Field type for LongField
    #  * @see db.LongField
    #  */
    # static final byte LONG_TYPE = 3;

    # /**
    #  * Field type for StringField
    #  * @see db.StringField
    #  */
    # static final byte STRING_TYPE = 4;

    # /**
    #  * Field type for BinaryField
    #  * @see db.BinaryField
    #  */
    # static final byte BINARY_OBJ_TYPE = 5;

    # /**
    #  * Field type for BooleanField
    #  * @see db.BooleanField
    #  */
    # static final byte BOOLEAN_TYPE = 6;

    # /**
    #  * Field type for 10-byte binary FixedField(10)
    #  * @see db.FixedField
    #  */
    # static final byte FIXED_10_TYPE = 7;

    # /**
    #  * Legacy Index Primary Key Field type for LongField
    #  * which was previously a boolean indicator for an index 
    #  * field with assumed long primary key.  Applies only 
    #  * to upper-nibble.  This value in the lower-nibble
    #  * is reserved for use in the special-purpose byte value 0x88.
    #  * (see {@link LegacyIndexField})
    #  */
    # static final byte LEGACY_INDEX_LONG_TYPE = 8;

    # // Available field types (6): 0x9..0xE

    # /**
    #  * Reserved field encoding.  Intended for special purpose 
    #  * schema used (e.g.
    #  */
    # static final byte FIELD_RESERVED_15_TYPE = 0xf;

    # /**
    #  * Field base type mask
    #  */
    # static final byte FIELD_TYPE_MASK = (byte) 0x0F;

    # /**
    #  * Field index primary key type mask
    #  */
    # static final byte INDEX_PRIMARY_KEY_TYPE_MASK = (byte) ~FIELD_TYPE_MASK;
    INDEX_PRIMARY_KEY_TYPE_MASK = ~FIELD_TYPE_MASK

    # /**
    #  * Index Primary Key Field Type Shift 
    #  */
    # static final int INDEX_FIELD_TYPE_SHIFT = 4;
    INDEX_FIELD_TYPE_SHIFT = 4

    # private final boolean immutable;

    # /**
    #  * Abstract Field Constructor for a mutable instance
    #  */
    # Field() {
    # 	immutable = false;
    # }
    def __init__(self, immutable:bool = False):
        self.immutable = immutable
 

    # /**
    #  * Abstract Field Constructor
    #  * @param immutable true if field value is immutable
    #  */
    # Field(boolean immutable) {
    # 	this.immutable = immutable;
    # }

    # void checkImmutable() {
    # 	if (immutable) {
    # 		throw new IllegalFieldAccessException("immutable field instance");
    # 	}
    # }
    @abstractmethod
    def checkImmutable(self):
        if self.immutable:
            raise IllegalFieldAccessException("immutable field instance")

    # /**
    #  * Get field as a long value.
    #  * All fixed-length field objects must implement this method
    #  * @return long value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public long getLongValue() {
    # 	throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def getLongValue(self):
        raise IllegalFieldAccessException()

    # /**
    #  * Set field's long value.
    #  * All fixed-length field objects must implement this method
    #  * @param value long value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public void setLongValue(long value) {
    # 	throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def setLongValue(self, value):
        raise IllegalFieldAccessException()

    # /**
    #  * Get field as an integer value.
    #  * @return integer value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public int getIntValue() {
    # 	throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def getIntValue(self):
        raise IllegalFieldAccessException()

    # /**
    #  * Set field's integer value.
    #  * @param value integer value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public void setIntValue(int value) {
    #     throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def setIntValue(self, value):
        raise IllegalFieldAccessException()

    # /**
    #  * Get field as a short value.
    #  * @return short value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public short getShortValue() {
    #     throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def getShortValue(self):
        raise IllegalFieldAccessException()

    # /**
    #  * Set field's short value.
    #  * @param value short value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public void setShortValue(short value) {
    #     throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def setShortValue(self, value):
        raise IllegalFieldAccessException() 

    # /**
    #  * Get field as a byte value.
    #  * @return byte value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public byte getByteValue() {
    #     throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def getByteValue(self):
        raise IllegalFieldAccessException()

    # /**
    #  * Set field's byte value.
    #  * @param value byte value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public void setByteValue(byte value) {
    #     throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def setByteValue(self, value):
        raise IllegalFieldAccessException()

    # /**
    #  * Get field as a boolean value.
    #  * @return boolean value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public boolean getBooleanValue() {
    #     throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def getBooleanValue(self):
        raise IllegalFieldAccessException()

    # /**
    #  * Set field's boolean value.
    #  * @param value boolean value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public void setBooleanValue(boolean value) {
    #     throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def setBooleanValue(self, value):
        raise IllegalFieldAccessException()

    # /**
    #  * Get data as a byte array.
    #  * @return byte[]
    #  */
    # abstract public byte[] getBinaryData();
    @abstractmethod
    def getBinaryData(self):
        pass

    # /**
    #  * Set data from binary byte array.
    #  * All variable-length fields must implement this method.
    #  * @param bytes field data
    #  * @throws IllegalFieldAccessException if error occurs while reading bytes
    #  * into field which will generally be caused by the incorrect number of 
    #  * bytes provided to a fixed-length field.
    #  */
    # abstract public void setBinaryData(byte[] bytes);
    @abstractmethod
    def setBinaryData(self, bytes):
        pass

    # /**
    #  * Get field as a String value.
    #  * @return String value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public String getString() {
    #     throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def getString(self):
        raise IllegalFieldAccessException()

    # /**
    #  * Set field's String value.
    #  * @param str String value
    #  * @throws IllegalFieldAccessException thrown if method is not supported by specific
    #  * Field instance.
    #  */
    # public void setString(String str) {
    #     throw new IllegalFieldAccessException();
    # }
    @abstractmethod
    def setString(self, str: str):
        raise IllegalFieldAccessException()

    # /**
    #  * Truncate a variable length field to the specified length.
    #  * If current length is shorterm, this method has no affect.
    #  * @param length truncated length
    #  */
    # void truncate(int length) {
    #     throw new UnsupportedOperationException("Field may not be truncated");
    # }
    @abstractmethod
    def truncate(self, length: int):
        raise UnsupportedOperationException("Field may not be truncated")

    # /**
    #  * @return true if a Field instance is variable length, else false.
    #  */
    # public boolean isVariableLength() {
    #     return false;
    # }
    @abstractmethod
    def isVariableLength(self):
        return False

    # /**
    #  * Determine if specified field is same type as this field
    #  * @param field a Field instance
    #  * @return true if field is same type as this field
    #  */
    # public boolean isSameType(Field field) {
    #     return field != null && field.getClass() == getClass();
    # }
    @abstractmethod
    def isSameType(self, field: Self):
        return field is not None and field.__class__ == self.__class__

    # /**
    #  * Create new instance of this field with the same value.
    #  * @return new field instance with same value
    #  */
    # public abstract Field copyField();
    @abstractmethod
    def copyField(self):
        pass

    # /**
    #  * Create new instance of this field type.
    #  * @return new field instance with undefined initial value
    #  */
    # public abstract Field newField();
    @abstractmethod
    def newField(self):
        pass

    # /**
    #  * Return Field instance type as an integer value.
    #  * @return encoded field type
    #  */
    # abstract byte getFieldType();
    @abstractmethod
    def getFieldType(self):
        pass

    # /**
    #  * Write the field to buf at the specified offset.  When writing variable length 
    #  * fields, the length preceeds the actual data. 
    #  * @param buf data buffer
    #  * @param offset data offset
    #  * @return next available Field offset within buffer, or -1 if end of buffer reached.
    #  * @throws IndexOutOfBoundsException if invalid offset is specified
    #  * @throws IOException thrown if IO error occurs
    #  */
    # abstract int write(Buffer buf, int offset) throws IndexOutOfBoundsException, IOException;
    @abstractmethod
    def write(self, buf: Buffer, offset: int) -> int:
        pass

    # /**
    #  * Read the field value from buf at the specified offset. When reading variable length 
    #  * fields, the length preceeds the actual data. 
    #  * @param buf data buffer
    #  * @param offset data offset
    #  * @return next Field offset within buffer, or -1 if end of buffer reached.
    #  * @throws IndexOutOfBoundsException if invalid offset is specified
    #  * @throws IOException thrown if IO error occurs
    #  */
    # abstract int read(Buffer buf, int offset) throws IndexOutOfBoundsException, IOException;
    @abstractmethod
    def read(self, buf: Buffer, offset: int) -> int:
        pass

    # /**
    #  * Get the total number of bytes which will be read from the buffer
    #  * for this field.  For variable-length fields, only the length 
    #  * portion of the data is examined within the buffer.  This method is intended
    #  * to be used instead of the read method when only interested in the data 
    #  * length.
    #  * @param buf data buffer
    #  * @param offset data offset
    #  * @return total number of bytes for this field stored within buf
    #  * @throws IndexOutOfBoundsException if invalid offset is specified
    #  * @throws IOException thrown if IO error occurs
    #  */
    # abstract int readLength(Buffer buf, int offset) throws IndexOutOfBoundsException, IOException;
    @abstractmethod
    def readLength(self, buf: Buffer, offset: int) -> int:
        pass

    # /**
    #  * Get the number of bytes required to store this field value.
    #  * For a variable length fields, this value also accounts for a 4-byte
    #  * length prefix.  Additionally, this method should not be invoked when 
    #  * working with stored data until after the read method has been invoked.
    #  * @return total storage length
    #  */
    # abstract int length();
    @abstractmethod
    def length(self) -> int:
        pass

    # /**
    #  * Determine if the specified Object is another Field which has the same 
    #  * type and value as this Field.  When comparing a {@link PrimitiveField},
    #  * with a null state, a value of zero (0) is used.
    #  * @param obj another object
    #  * @return true if this field equals obj
    #  */
    # @Override
    # public abstract boolean equals(Object obj);
    @abstractmethod
    def equals(self, object: object) -> bool:
        pass

    # @Override
    # public abstract int hashCode();
    @abstractmethod
    def hashCode(self) -> int:
        pass

    # /**
    #  * Get field value as a formatted string
    #  * @return field value string
    #  */
    # public abstract String getValueAsString();
    @abstractmethod
    def getValueAsString(self) -> str:
        pass

    # /**
    #  * Get minimum field value.
    #  * 
    #  * Supported for fixed-length fields only.
    #  * @return minimum value
    #  * @throws UnsupportedOperationException if field is not fixed-length
    #  */
    # abstract Field getMinValue();
    @abstractmethod
    def getMinValue(self) -> Self:
        pass

    # /**
    #  * Get maximum field value.
    #  * 
    #  * Supported for fixed-length fields only.
    #  * @return maximum value
    #  * @throws UnsupportedOperationException if field is not fixed-length
    #  */
    # abstract Field getMaxValue();
    @abstractmethod
    def getMaxValue(self) -> Self:
        pass

    # /**
    #  * Determine if the field has been set to a null-state or value.  
    #  * @return true if field has been set to a null state or value, else false
    #  */
    # public abstract boolean isNull();
    @abstractmethod
    def isNull(self) -> bool:
        pass

    # /**
    #  * Set this field to its null-state.  For variable-length field this will 
    #  * generally correspond to a null value, while primitive and fixed-length
    #  * fields will be set to a zero (0) value.  This method may only be invoked
    #  * on a sparse column field.
    #  * @throws IllegalFieldAccessException thrown if this field is immutable or is an index field
    #  */
    # abstract void setNull();
    @abstractmethod
    def setNull(self) -> None:
        pass

    # /**
    #  * Performs a fast in-place comparison of this field value with another
    #  * field value stored within the specified buffer at the the specified offset.
    #  * NOTE: This method will treat all null primitives as 0 although is not intended
    #  * to support such use.
    #  * @param buffer data buffer
    #  * @param offset field value offset within buffer
    #  * @return comparison value, zero if equal, -1 if this field has a value 
    #  * less than the stored field, or +1 if this field has a value greater than 
    #  * the stored field located at keyIndex.
    #  * @throws IndexOutOfBoundsException if invalid offset is specified
    #  */
    # abstract int compareTo(DataBuffer buffer, int offset) throws IndexOutOfBoundsException;
    @abstractmethod
    def compare_to_databuffer(self, buffer: DataBuffer, offset: int) -> int:
        pass

    # /**
    #  * Compares this Field with another Field for order.  Returns a
    #  * negative integer, zero, or a positive integer as this object is less
    #  * than, equal to, or greater than the specified Field.  
    #  * <br>
    #  * NOTE: Field objects do not fully comply with the Comparable interface.
    #  * Only the same Field implementations may be compared.  In addition, the 
    #  * null state is not considered when comparing {@link PrimitiveField}s which have a 
    #  * zero (0) value.
    #  * @param otherField another Field which is the same type as this Field
    #  * @return field comparison result (see {@link Comparable#compareTo(Object)}).
    #  * @throws ClassCastException if an attempt to compare dissimilar Fields (e.g., 
    #  * an IntField may not be compared with a ShortField).
    #  */
    # @Override
    # public abstract int compareTo(Field otherField);
    @abstractmethod
    def compare_to_field(self, otherField: Self) -> int:
        pass

    # /**
    #  * Get the field associated with the specified type value.
    #  * @param fieldType field type index
    #  * @return Field field instance which corresponds to the specified fieldType
    #  * @throws UnsupportedFieldException if unsupported fieldType specified
    #  */
    # static Field getField(byte fieldType) throws UnsupportedFieldException {
    #     if (fieldType == 0x88) {
    #         // 0x88 - Reserved value (future expanded Field encoding)
    #         throw new UnsupportedFieldException(fieldType);
    #     }
    #     if ((fieldType & INDEX_PRIMARY_KEY_TYPE_MASK) == 0) {
    #         switch (fieldType & FIELD_TYPE_MASK) {
    #             case LONG_TYPE:
    #                 return LongField.INSTANCE;
    #             case INT_TYPE:
    #                 return IntField.INSTANCE;
    #             case STRING_TYPE:
    #                 return StringField.INSTANCE;
    #             case SHORT_TYPE:
    #                 return ShortField.INSTANCE;
    #             case BYTE_TYPE:
    #                 return ByteField.INSTANCE;
    #             case BOOLEAN_TYPE:
    #                 return BooleanField.INSTANCE;
    #             case BINARY_OBJ_TYPE:
    #                 return BinaryField.INSTANCE;
    #             case FIXED_10_TYPE:
    #                 return FixedField10.INSTANCE;
    #         }
    #     }
    #     else {
    #         return IndexField.getIndexField(fieldType);
    #     }
    #     throw new UnsupportedFieldException(fieldType);
    # }
    @classmethod
    def getField(cls, fieldType: int) -> Self:
        if fieldType == 0x88:
            raise UnsupportedFieldException(fieldType)
        if (fieldType & cls.INDEX_PRIMARY_KEY_TYPE_MASK) == 0: 
            if fieldType & cls.FIELD_TYPE_MASK == cls.LONG_TYPE:
                return LongField.INSTANCE
            if fieldType & cls.FIELD_TYPE_MASK == cls.INT_TYPE:
                return IntField.INSTANCE
            if fieldType & cls.FIELD_TYPE_MASK == cls.STRING_TYPE:
                return StringField.INSTANCE
            if fieldType & cls.FIELD_TYPE_MASK == cls.SHORT_TYPE:
                return ShortField.INSTANCE
            if fieldType & cls.FIELD_TYPE_MASK == cls.BYTE_TYPE:
                return ByteField.INSTANCE
            if fieldType & cls.FIELD_TYPE_MASK == cls.BOOLEAN_TYPE:
                return BooleanField.INSTANCE
            if fieldType & cls.FIELD_TYPE_MASK == cls.BINARY_OBJ_TYPE:
                return BinaryField.INSTANCE
            if fieldType & cls.FIELD_TYPE_MASK == cls.FIXED_10_TYPE:
                return FixedField10.INSTANCE
        else:
            return IndexField.getIndexField(fieldType)
        raise UnsupportedFieldException(fieldType)

    # public static class UnsupportedFieldException extends IOException {
    #     UnsupportedFieldException(byte fieldType) {
    #         super("Unsupported DB field type: 0x" + Integer.toHexString(fieldType & 0xff));
    #     }

    #     UnsupportedFieldException(String msg) {
    #         super(msg);
    #     }
    # }
    class UnsupportedFieldException(Exception):
        def __init__(self, fieldType: Optional[int]=None, msg: Optional[str]=None):
            # super().__init__("Unsupported DB field type: 0x" + hex(fieldType & 0xff))
            if msg is not None:
                super().__init__(msg)
            if fieldType is not None:
                super().__init__("Unsupported DB field type: 0x" + hex(fieldType & 0xff))

    # /**
    #  * Get the type index value of the FixedField type which corresponds
    #  * to the specified fixed-length;
    #  * @param fixedLength fixed length (currently only 10 is supported)
    #  * @return FixedLength field type index
    #  * @throws IllegalArgumentException if unsupported fixedLength is specified
    #  */
    # static byte getFixedType(int fixedLength) {
    #     if (fixedLength == 10) {
    #         return FIXED_10_TYPE;
    #     }
    #     throw new IllegalArgumentException(
    #         "Unsupported fixed-length binary type size: " + fixedLength);
    # }
    @staticmethod
    def getFixedType(fixedLength: int) -> int:
        if fixedLength == 10:
            return cls.FIXED_10_TYPE
        raise IllegalArgumentException("Unsupported fixed-length binary type size: " + fixedLength)

    # /**
    #  * Get a fixed-length field of the specified size
    #  * @param size fixed-field length (supported sizes: 1, 4, 8, 10)
    #  * @return fixed field instance
    #  * @throws IllegalArgumentException if unsupported fixed field length
    #  */
    # static Field getFixedField(int size) {
    #     switch (size) {
    #         case 1:
    #             return new ByteField();
    #         case 4:
    #             return new IntField();
    #         case 8:
    #             return new LongField();
    #         case 10:
    #             return new FixedField10();
    #     }
    #     throw new IllegalArgumentException("Unsupported fixed-field length: " + size);
    # }
    @classmethod
    def getFixedField(cls, size: int) -> Self:
        if size == 1:
            return ByteField()
        if size == 4:
            return IntField()
        if size == 8:
            return LongField()
        if size == 10:
            return FixedField10()
        raise IllegalArgumentException("Unsupported fixed-field length: " + size)

    # /**
    #  * Determine if a specified field instance may be indexed
    #  * @param field field to be checked
    #  * @return true if field can be indexed
    #  */
    # public static boolean canIndex(Field field) {
    #     if (field == null) {
    #         return false;
    #     }
    #     if (field instanceof IndexField) {
    #         return false;
    #     }
    #     return !field.isSameType(BooleanField.INSTANCE) && !field.isSameType(ByteField.INSTANCE);
    # }
    @classmethod
    def canIndex(cls, field: Self) -> bool:
        if field is None:
            return False
        if isinstance(field, IndexField):
            return False
        return not field.isSameType(BooleanField.INSTANCE) and not field.isSameType(ByteField.INSTANCE)

}
