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

# import java.io.IOException;
# import java.util.Arrays;

# import db.buffers.DataBuffer;

# /**
#  * <code>BinaryField</code> provides a wrapper for variable length binary data which is read or
#  * written to a Record.
#  */
# public class BinaryField extends Field {
from ctypes import c_byte
from typing import List, Optional, Self

from .buffer import Buffer
from .field import Field
from .data_buffer import DataBuffer


class BinaryField(Field):

    # /**
    #  * Instance intended for defining a {@link Table} {@link Schema}
    #  */
    # public static final BinaryField INSTANCE = new BinaryField(null, true);
    # TODO

    # protected byte[] data;
    # private Integer hashcode;

    # /**
    #  * Construct a binary data field with an initial value of null.
    #  */
    # public BinaryField() {
    # }
    def __init__(self):
        self.data: Optional[bytes] = None
        self.hashcode: Optional[int] = None
        self.immutable: Optional[bool] = None

    # /**
    #  * Construct a binary data field with an initial value of data.
    #  * @param data initial value
    #  */
    # public BinaryField(byte[] data) {
    # 	this(data, false);
    # }
    @classmethod
    def from_bytes(cls, data: bytes):
        x = cls()
        x.data = data

    # /**
    #  * Construct a binary data field with an initial value of data.
    #  * @param data initial value
    #  * @param immutable true if field value is immutable
    #  */
    # BinaryField(byte[] data, boolean immutable) {
    # 	super(immutable);
    # 	this.data = data;
    # }
    @classmethod
    def from_bytes_immutable(cls, data: bytes, immutable: bool):
        x = cls()
        x.data = data
        x.immutable = immutable

    # @Override
    # public boolean isNull() {
    # 	return data == null;
    # }
    def is_null(self) -> bool:
        return self.data is None

    # @Override
    # void setNull() {
    # 	checkImmutable();
    # 	data = null;
    # }
    def set_null(self):
        self.check_immutable()
        self.data = None

    # @Override
    # void checkImmutable() {
    # 	super.checkImmutable();
    # 	hashcode = null;
    # }
    def check_immutable(self):
        super().check_immutable()
        self.hashcode = None

    # @Override
    # public byte[] getBinaryData() {
    # 	return data;
    # }
    def get_binary_data(self) -> Optional[bytes]:
        return self.data

    # @Override
    # public void setBinaryData(byte[] data) {
    # 	checkImmutable();
    # 	this.data = data;
    # }
    def set_binary_data(self, data: Optional[bytes]):
        self.check_immutable()
        self.data = data

    # @Override
    # int length() {
    # 	return (data == null) ? 4 : (data.length + 4);
    # }
    def length(self) -> int:
        return 4 if self.data is None else len(self.data) + 4

    # @Override
    # int write(Buffer buf, int offset) throws IndexOutOfBoundsException, IOException {
    # 	if (data == null) {
    # 		return buf.putInt(offset, -1);
    # 	}
    # 	offset = buf.putInt(offset, data.length);
    # 	return buf.put(offset, data);
    # }
    def write(self, buf: Buffer, offset: int) -> int:
        if self.data is None:
            return buf.putInt(offset, -1)
        offset = buf.putInt(offset, len(self.data))
        return buf.put(offset, self.data)

    # @Override
    # int read(Buffer buf, int offset) throws IndexOutOfBoundsException, IOException {
    #     checkImmutable();
    #     int len = buf.getInt(offset);
    #     offset += 4;
    #     if (len < 0) {
    #         data = null;
    #     }
    #     else {
    #         data = buf.get(offset, len);
    #         offset += len;
    #     }
    #     return offset;
    # }
    def read(self, buf: Buffer, offset: int) -> int:
        self.check_immutable()
        len = buf.getInt(offset)
        offset += 4
        if len < 0:
            self.data = None
        else:
            self.data = buf.get(offset, len)
            offset += len
        return offset

    # @Override
    # int readLength(Buffer buf, int offset) throws IndexOutOfBoundsException, IOException {
    #     int len = buf.getInt(offset);
    #     return (len < 0 ? 0 : len) + 4;
    # }
    def read_length(self, buf: Buffer, offset: int) -> int:
        len = buf.getInt(offset)
        return 0 if len < 0 else len + 4

    # @Override
    # public boolean isVariableLength() {
    #     return true;
    # }
    def is_variable_length(self) -> bool:
        return True

    # @Override
    # byte getFieldType() {
    #     return BINARY_OBJ_TYPE;
    # }
    def get_field_type(self) -> int:
        return BINARY_OBJ_TYPE

    # @Override
    # void truncate(int length) {
    #     checkImmutable();
    #     int maxLen = length - 4;
    #     if (data != null && data.length > maxLen) {
    #         byte[] newData = new byte[maxLen];
    #         System.arraycopy(data, 0, newData, 0, maxLen);
    #         data = newData;
    #     }
    # }
    def get_field_type(self, length: int):
        self.check_immutable()
        max_len = length - 4
        if self.data is not None and len(self.data) > max_len:
            self.data = self.data[:max_len]

    # @Override
    # public int compareTo(Field o) {
    #     BinaryField f = (BinaryField) o;
    #     if (data == null) {
    #         if (f.data == null) {
    #             return 0;
    #         }
    #         return -1;
    #     }
    #     else if (f.data == null) {
    #         return 1;
    #     }

    #     int len1 = data.length;
    #     int len2 = f.data.length;
    #     int offset1 = 0;
    #     int offset2 = 0;
    #     int n = Math.min(len1, len2);
    #     while (n-- != 0) {
    #         int b1 = data[offset1++] & 0xff;
    #         int b2 = f.data[offset2++] & 0xff;
    #         if (b1 != b2) {
    #             return b1 - b2;
    #         }
    #     }
    #     return len1 - len2;
    # }
    def compare_to(self, o: Field) -> int:
        f = o
        if self.data is None:
            if f.data is None:
                return 0
            return -1
        elif f.data is None:
            return 1

        len1 = len(self.data)
        len2 = len(f.data)
        offset1 = 0
        offset2 = 0
        n = min(len1, len2)
        while n != 0:
            b1 = self.data[offset1] & 0xFF
            b2 = f.data[offset2] & 0xFF
            if b1 != b2:
                return b1 - b2
            offset1 += 1
            offset2 += 1
            n -= 1
        return len1 - len2

    # @Override
    # int compareTo(DataBuffer buffer, int offset) {
    #     int len = buffer.getInt(offset);
    #     if (data == null) {
    #         if (len < 0) {
    #             return 0;
    #         }
    #         return -1;
    #     }
    #     else if (len < 0) {
    #         return 1;
    #     }

    #     return -buffer.unsignedCompareTo(data, offset + 4, len);
    def compare_to_buffer(self, buffer: DataBuffer, offset: int) -> int:
        # }
        len = buffer.getInt(offset)
        if self.data is None:
            if len < 0:
                return 0
            return -1
        elif len < 0:
            return 1

        return -buffer.unsignedCompareTo(self.data, offset + 4, len)

    # @Override
    # public BinaryField copyField() {
    #     if (isNull()) {
    #         return new BinaryField();
    #     }
    #     return new BinaryField(getBinaryData().clone());
    # }
    def copy_field(self) -> Field:
        if self.is_null():
            return Self()
        return Self(self.get_binary_data().copy())

    # @Override
    # public BinaryField newField() {
    #     return new BinaryField();
    # }
    @classmethod
    def new_field(cls) -> Self:
        return cls()

    # @Override
    # BinaryField getMinValue() {
    #     throw new UnsupportedOperationException();
    # }
    def get_min_value(self) -> Self:
        raise NotImplementedError()

    # @Override
    # BinaryField getMaxValue() {
    #     throw new UnsupportedOperationException();
    # }
    def get_max_value(self) -> Self:
        raise NotImplementedError()

    # @Override
    # public boolean equals(Object obj) {
    #     if (obj == null || obj.getClass() != getClass()) {
    #         return false;
    #     }
    #     BinaryField f = (BinaryField) obj;
    #     return Arrays.equals(f.data, data);
    # }
    def __eq__(self, obj: object) -> bool:
        if (
            obj is None
            or obj.__class__ != self.__class__
            or not isinstance(obj, self.__class__)
        ):
            return False
        f: Self = obj
        return f.data == self.data

    # @Override
    # public int hashCode() {
    #     if (hashcode == null) {
    #         int h = 0;
    #         if (data != null) {
    #             for (byte b : data) {
    #                 h = 31 * h + (b & 0xff);
    #             }
    #         }
    #         hashcode = h;
    #     }
    #     return hashcode;
    # }
    def __hash__(self) -> int:
        if self.hashcode is None:
            h = 0
            if self.data is not None:
                for b in self.data:
                    h = 31 * h + (b & 0xFF)
            self.hashcode = h
        return self.hashcode

    # /// Methods below should not use data field directly

    # @Override
    # public String toString() {
    #     String classname = getClass().getSimpleName();
    #     String nullState = "";
    #     if (isNull()) {
    #         nullState = "(NULL)";
    #     }
    #     byte[] d = getBinaryData();
    #     if (d == null) {
    #         return classname + nullState + ": null";
    #     }
    #     return classname + nullState + ": [" + d.length + "] = 0x" + getValueAsString(d);
    # }
    def __str__(self) -> str:
        classname: str = self.__class__.__name__
        null_state = ""
        if self.is_null():
            null_state = "(NULL)"
        d = self.get_binary_data()
        if d is None:
            return f"{classname} {null_state}: null"
        return f"{classname} {null_state}: [{len(d)}] = 0x{self.get_bytes_as_string(d)}"

    # @Override
    # public String getValueAsString() {
    #     byte[] d = getBinaryData();
    #     if (d == null) {
    #         return "null";
    #     }
    #     return "{" + getValueAsString(d) + "}";
    # }
    def get_value_as_string(self) -> str:
        d = self.get_binary_data()
        if d is None:
            return "null"
        return "{" + self.get_bytes_as_string(d) + "}"

    # /**
    #  * Get format value string for byte array
    #  * @param data byte array
    #  * @return formatted value string
    #  */
    # public static String getValueAsString(byte[] data) {
    #     StringBuffer buf = new StringBuffer();
    #     int i = 0;
    #     for (; i < 24 && i < data.length; i++) {
    #         String b = Integer.toHexString(data[i] & 0xff);
    #         if (b.length() == 1) {
    #             buf.append('0');
    #         }
    #         buf.append(b);
    #         buf.append(' ');
    #     }
    #     if (i < data.length) {
    #         buf.append("...");
    #     }
    #     return buf.toString();
    # }
    def get_bytes_as_string(self, data: bytes) -> str:
        # buf = []
        buf: str = ""
        i = 0
        while i < 24 and i < len(data):
            b = data[i] & 0xFF
            # buf.append(f"{b:02x} ")
            buf += f"{b:02x} "
            i += 1
        if i < len(data):
            # buf.append("...")
            buf += "..."
        return "".join(buf)


# }
