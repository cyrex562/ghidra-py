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

# import java.io.UnsupportedEncodingException;
# import java.util.ArrayList;

# import ghidra.util.exception.AssertException;

# /**
#  * Allows various non-database supported data types to be
#  * encoded within a BinaryField which may be stored within the
#  * database.
#  * <p>
#  * Although the BinaryField stores a byte array, this type
#  * is supported by this class so that the use of a BinaryField
#  * within a table can always relate to this class and still
#  * support a byte array.
#  */
# public class BinaryCodedField extends BinaryField {
# from ctypes.wintypes import BYTE, DOUBLE
from .binary_field import BinaryField

class BinaryCodedField(BinaryField):

    # /**
    #  * byte[] data type
    #  */
    # public static final byte BYTE_ARRAY = 0;
    BYTE_ARRAY = 0

    # /**
    #  * float data type
    #  */
    # public static final byte FLOAT = 1;
    FLOAT = 1

    # /**
    #  * double data type
    #  */
    # public static final byte DOUBLE = 2;
    DOUBLE = 2

    # /**
    #  * short data type
    #  */
    # public static final byte SHORT_ARRAY = 3;
    SHORT_ARRAY = 3

    # /**
    #  * int[] data type
    #  */
    # public static final byte INT_ARRAY = 4;
    INT_ARRAY = 4

    # /**
    #  * long[] data type
    #  */
    # public static final byte LONG_ARRAY = 5;
    LONG_ARRAY = 5

    # /**
    #  * float[] data type
    #  */
    # public static final byte FLOAT_ARRAY = 6;
    FLOAT_ARRAY = 6

    # /**
    #  * double[] data type
    #  */
    # public static final byte DOUBLE_ARRAY = 7;
    DOUBLE_ARRAY = 7

    # /**
    #  * String[] data type
    #  */
    # public static final byte STRING_ARRAY = 8;
    STRING_ARRAY = 8

    # private static final int DATA_TYPE_OFFSET = 0;
    DATA_TYPE_OFFSET = 0
    # private static final int DATA_OFFSET = 1;
    DATA_OFFSET = 1

    # private static final String STRING_ENCODING = "UTF-8";
    STRING_ENCODING = "UTF-8"

    # /**
    #  * Default constructor
    #  */
    # BinaryCodedField() {
    # }
    def __init__(self):
        pass
    
    # /**
    #  * Construct a coded field from an existing binary field.
    #  * @param binField the binary field
    #  */
    # public BinaryCodedField(BinaryField binField) {
    #     data = binField.getBinaryData();
    # }
    def from_bin_field(self, binField):
        self.data = binField.getBinaryData()

    # /**
    #  * Construct a coded field from a double value.
    #  * @param value the double value
    #  */
    # public BinaryCodedField(double value) {
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(9);
    #     buffer.putByte(DATA_TYPE_OFFSET, DOUBLE);
    #     buffer.putLong(DATA_OFFSET, Double.doubleToLongBits(value));
    #     data = buffer.getData();
    # }
    def from_double(self, value):
        buffer = BinaryDataBuffer(9)
        buffer.putByte(self.DATA_TYPE_OFFSET, self.DOUBLE)
        buffer.putLong(self.DATA_OFFSET, Double.doubleToLongBits(value))
        self.data = buffer.getData()

    # /**
    #  * Construct a coded field from a float value.
    #  * @param value the float value
    #  */
    # public BinaryCodedField(float value) {
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(5);
    #     buffer.putByte(DATA_TYPE_OFFSET, FLOAT);
    #     buffer.putInt(DATA_OFFSET, Float.floatToIntBits(value));
    #     data = buffer.getData();
    # }
    def from_float(self, value):
        buffer = BinaryDataBuffer(5)
        buffer.putByte(self.DATA_TYPE_OFFSET, self.FLOAT)
        buffer.putInt(self.DATA_OFFSET, Float.floatToIntBits(value))
        self.data = buffer.getData()

    # /**
    #  * Construct a coded field from a byte array.
    #  * @param values byte array
    #  */
    # public BinaryCodedField(byte[] values) {
    #     if (values != null) {
    #         data = new byte[values.length + 2];
    #         data[DATA_OFFSET] = (byte) 0;
    #         System.arraycopy(values, 0, data, 2, values.length);
    #     }
    #     else {
    #         data = new byte[2];
    #         data[DATA_OFFSET] = (byte) -1;
    #     }
    #     data[DATA_TYPE_OFFSET] = BYTE_ARRAY;
    # }
    def from_bytes(self, values):
        if values is not None:
            self.data = [0] * (len(values) + 2)
            self.data[self.DATA_OFFSET] = 0
            self.data[2:] = values
        else:
            self.data = [0] * 2
            self.data[self.DATA_OFFSET] = -1
        self.data[self.DATA_TYPE_OFFSET] = self.BYTE_ARRAY

    # /**
    #  * Construct a coded field from a short array.
    #  * @param values short array
    #  */
    # public BinaryCodedField(short[] values) {
    #     int len = (values != null ? (2 * values.length) : 0) + 2;
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(len);
    #     buffer.putByte(DATA_TYPE_OFFSET, SHORT_ARRAY);
    #     if (values != null) {
    #         int offset = DATA_OFFSET;
    #         buffer.putByte(offset++, (byte) 0);
    #         for (int i = 0; i < values.length; i++) {
    #             offset = buffer.putShort(offset, values[i]);
    #         }
    #     }
    #     else {
    #         buffer.putByte(DATA_OFFSET, (byte) -1);
    #     }
    #     data = buffer.getData();
    # }
    def from_short_array(self, values):
        len = (len(values) * 2) if values is not None else 0 + 2
        buffer = BinaryDataBuffer(len)
        buffer.putByte(self.DATA_TYPE_OFFSET, self.SHORT_ARRAY)
        if values is not None:
            offset = self.DATA_OFFSET
            buffer.putByte(offset, 0)
            for i in range(len(values)):
                offset = buffer.putShort(offset, values[i])
        else:
            buffer.putByte(self.DATA_OFFSET, -1)
        self.data = buffer.getData()

    # /**
    #  * Construct a coded field from a int array.
    #  * @param values int array
    #  */
    # public BinaryCodedField(int[] values) {
    #     int len = (values != null ? (4 * values.length) : 0) + 2;
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(len);
    #     buffer.putByte(DATA_TYPE_OFFSET, INT_ARRAY);
    #     if (values != null) {
    #         int offset = DATA_OFFSET;
    #         buffer.putByte(offset++, (byte) 0);
    #         for (int i = 0; i < values.length; i++) {
    #             offset = buffer.putInt(offset, values[i]);
    #         }
    #     }
    #     else {
    #         buffer.putByte(DATA_OFFSET, (byte) -1);
    #     }
    #     data = buffer.getData();
    # }
    def from_int_array(self, values):
        len = (len(values) * 4) if values is not None else 0 + 2
        buffer = BinaryDataBuffer(len)
        buffer.putByte(self.DATA_TYPE_OFFSET, self.INT_ARRAY)
        if values is not None:
            offset = self.DATA_OFFSET
            buffer.putByte(offset, 0)
            for i in range(len(values)):
                offset = buffer.putInt(offset, values[i])
        else:
            buffer.putByte(self.DATA_OFFSET, -1)
        self.data = buffer.getData()

    # /**
    #  * Construct a coded field from a long array.
    #  * @param values long array
    #  */
    # public BinaryCodedField(long[] values) {
    #     int len = (values != null ? (8 * values.length) : 0) + 2;
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(len);
    #     buffer.putByte(DATA_TYPE_OFFSET, LONG_ARRAY);
    #     if (values != null) {
    #         int offset = DATA_OFFSET;
    #         buffer.putByte(offset++, (byte) 0);
    #         for (int i = 0; i < values.length; i++) {
    #             offset = buffer.putLong(offset, values[i]);
    #         }
    #     }
    #     else {
    #         buffer.putByte(DATA_OFFSET, (byte) -1);
    #     }
    #     data = buffer.getData();
    # }
    def from_long_array(self, values):
        len = (len(values) * 8) if values is not None else 0 + 2
        buffer = BinaryDataBuffer(len)
        buffer.putByte(self.DATA_TYPE_OFFSET, self.LONG_ARRAY)
        if values is not None:
            offset = self.DATA_OFFSET
            buffer.putByte(offset, 0)
            for i in range(len(values)):
                offset = buffer.putLong(offset, values[i])
        else:
            buffer.putByte(self.DATA_OFFSET, -1)
        self.data = buffer.getData()

    # /**
    #  * Construct a coded field from a float array.
    #  * @param values float array
    #  */
    # public BinaryCodedField(float[] values) {
    #     int len = (values != null ? (4 * values.length) : 0) + 2;
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(len);
    #     buffer.putByte(DATA_TYPE_OFFSET, FLOAT_ARRAY);
    #     if (values != null) {
    #         int offset = DATA_OFFSET;
    #         buffer.putByte(offset++, (byte) 0);
    #         for (int i = 0; i < values.length; i++) {
    #             offset = buffer.putInt(offset, Float.floatToIntBits(values[i]));
    #         }
    #     }
    #     else {
    #         buffer.putByte(DATA_OFFSET, (byte) -1);
    #     }
    #     data = buffer.getData();
    # }
    def from_float_array(self, values):
        len = (len(values) * 4) if values is not None else 0 + 2
        buffer = BinaryDataBuffer(len)
        buffer.putByte(self.DATA_TYPE_OFFSET, self.FLOAT_ARRAY)
        if values is not None:
            offset = self.DATA_OFFSET
            buffer.putByte(offset, 0)
            for i in range(len(values)):
                offset = buffer.putInt(offset, Float.floatToIntBits(values[i]))
        else:
            buffer.putByte(self.DATA_OFFSET, -1)
        self.data = buffer.getData()

    # /**
    #  * Construct a coded field from a double array.
    #  * @param values double array
    #  */
    # public BinaryCodedField(double[] values) {
    #     int len = (values != null ? (8 * values.length) : 0) + 2;
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(len);
    #     buffer.putByte(DATA_TYPE_OFFSET, DOUBLE_ARRAY);
    #     if (values != null) {
    #         int offset = DATA_OFFSET;
    #         buffer.putByte(offset++, (byte) 0);
    #         for (int i = 0; i < values.length; i++) {
    #             offset = buffer.putLong(offset, Double.doubleToLongBits(values[i]));
    #         }
    #     }
    #     else {
    #         buffer.putByte(DATA_OFFSET, (byte) -1);
    #     }
    #     data = buffer.getData();
    # }
    def from_double_array(self, values):
        len = (len(values) * 8) if values is not None else 0 + 2
        buffer = BinaryDataBuffer(len)
        buffer.putByte(self.DATA_TYPE_OFFSET, self.DOUBLE_ARRAY)
        if values is not None:
            offset = self.DATA_OFFSET
            buffer.putByte(offset, 0)
            for i in range(len(values)):
                offset = buffer.putLong(offset, Double.doubleToLongBits(values[i]))
        else:
            buffer.putByte(self.DATA_OFFSET, -1)
        self.data = buffer.getData()

    # /**
    #  * Construct a coded field from a String array.
    #  * @param strings String array
    #  */
    # public BinaryCodedField(String[] strings) {
    #     BinaryDataBuffer buffer = null;
    #     if (strings != null) {
    #         int len = 2;
    #         for (int i = 0; i < strings.length; i++) {
    #             len += 4;
    #             if (strings[i] != null) {
    #                 len += strings[i].length();
    #             }
    #         }
    #         buffer = new BinaryDataBuffer(len);
    #         int offset = DATA_OFFSET;
    #         buffer.putByte(offset++, (byte) 0);
    #         try {
    #             for (int i = 0; i < strings.length; i++) {
    #                 if (strings[i] == null) {
    #                     offset = buffer.putInt(offset, -1);
    #                 }
    #                 else {
    #                     byte[] bytes = strings[i].getBytes(STRING_ENCODING);
    #                     offset = buffer.putInt(offset, bytes.length);
    #                     offset = buffer.put(offset, bytes);
    #                 }
    #             }
    #         }
    #         catch (UnsupportedEncodingException e) {
    #             throw new AssertException();
    #         }
    #     }
    #     else {
    #         buffer = new BinaryDataBuffer(2);
    #         buffer.putByte(DATA_OFFSET, (byte) -1);
    #     }
    #     buffer.putByte(DATA_TYPE_OFFSET, STRING_ARRAY);
    #     data = buffer.getData();
    # }
    def from_string_array(self, strings):
        buffer = None
        if strings is not None:
            len = 2
            for i in range(len(strings)):
                len += 4
                if strings[i] is not None:
                    len += len(strings[i])
            buffer = BinaryDataBuffer(len)
            offset = self.DATA_OFFSET
            buffer.putByte(offset, 0)
            try:
                for i in range(len(strings)):
                    if strings[i] is None:
                        offset = buffer.putInt(offset, -1)
                    else:
                        bytes = strings[i].encode(self.STRING_ENCODING)
                        offset = buffer.putInt(offset, len(bytes))
                        offset = buffer.put(offset, bytes)
            except UnsupportedEncodingException:
                raise AssertException()
        else:
            buffer = BinaryDataBuffer(2)
            buffer.putByte(self.DATA_OFFSET, -1)
        buffer.putByte(self.DATA_TYPE_OFFSET, self.STRING_ARRAY)
        self.data = buffer.getData()

    # /**
    #  * Get the data type associated with this field.
    #  * @return data type
    #  */
    # public byte getDataType() {
    #     return data[DATA_TYPE_OFFSET];
    # }
    def get_data_type(self):
        return self.data[self.DATA_TYPE_OFFSET]

    # /**
    #  * Get the double value contained with this field.
    #  * @return double value
    #  * @throws IllegalFieldAccessException if data type is not DOUBLE.
    #  */
    # public double getDoubleValue() {
    #     if (DOUBLE != data[DATA_TYPE_OFFSET]) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(data);
    #     return Double.longBitsToDouble(buffer.getLong(DATA_OFFSET));
    # }
    def get_double_value(self):
        if self.DOUBLE != self.data[self.DATA_TYPE_OFFSET]:
            raise IllegalFieldAccessException()
        buffer = BinaryDataBuffer(self.data)
        return Double.longBitsToDouble(buffer.getLong(self.DATA_OFFSET))

    # /**
    #  * Get the float value contained with this field.
    #  * @return float value
    #  * @throws IllegalFieldAccessException if data type is not FLOAT.
    #  */
    # public float getFloatValue() {
    #     if (FLOAT != data[DATA_TYPE_OFFSET]) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(data);
    #     return Float.intBitsToFloat(buffer.getInt(DATA_OFFSET));
    # }
    def get_float_value(self):
        if self.FLOAT != self.data[self.DATA_TYPE_OFFSET]:
            raise IllegalFieldAccessException()
        buffer = BinaryDataBuffer(self.data)
        return Float.intBitsToFloat(buffer.getInt(self.DATA_OFFSET))

    # /**
    #  * Get the byte array contained with this field.
    #  * @return byte array
    #  * @throws IllegalFieldAccessException if data type is not BYTE_ARRAY.
    #  */
    # public byte[] getByteArray() {
    #     if (BYTE_ARRAY != data[DATA_TYPE_OFFSET]) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     if (data[DATA_OFFSET] < 0) {
    #         return null;
    #     }
    #     byte[] values = new byte[data.length - 2];
    #     System.arraycopy(data, 2, values, 0, values.length);
    #     return values;
    # }
    def get_byte_array(self):
        if self.BYTE_ARRAY != self.data[self.DATA_TYPE_OFFSET]:
            raise IllegalFieldAccessException()
        if self.data[self.DATA_OFFSET] < 0:
            return None
        return self.data[2:]

    # /**
    #  * Get the short array contained with this field.
    #  * @return short array
    #  * @throws IllegalFieldAccessException if data type is not SHORT_ARRAY.
    #  */
    # public short[] getShortArray() {
    #     if (SHORT_ARRAY != data[DATA_TYPE_OFFSET]) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     if (data[DATA_OFFSET] < 0) {
    #         return null;
    #     }
    #     short[] values = new short[(data.length - 2) / 2];
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(data);
    #     int offset = DATA_OFFSET + 1;
    #     for (int i = 0; i < values.length; i++) {
    #         values[i] = buffer.getShort(offset);
    #         offset += 2;
    #     }
    #     return values;
    # }
    def get_short_array(self):
        if self.SHORT_ARRAY != self.data[self.DATA_TYPE_OFFSET]:
            raise IllegalFieldAccessException()
        if self.data[self.DATA_OFFSET] < 0:
            return None
        values = [0] * ((len(self.data) - 2) // 2)
        buffer = BinaryDataBuffer(self.data)
        offset = self.DATA_OFFSET + 1
        for i in range(len(values)):
            values[i] = buffer.getShort(offset)
            offset += 2
        return values

    # /**
    #  * Get the int array contained with this field.
    #  * @return int array
    #  * @throws IllegalFieldAccessException if data type is not INT_ARRAY.
    #  */
    # public int[] getIntArray() {
    #     if (INT_ARRAY != data[DATA_TYPE_OFFSET]) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     if (data[DATA_OFFSET] < 0) {
    #         return null;
    #     }
    #     int[] values = new int[(data.length - 2) / 4];
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(data);
    #     int offset = DATA_OFFSET + 1;
    #     for (int i = 0; i < values.length; i++) {
    #         values[i] = buffer.getInt(offset);
    #         offset += 4;
    #     }
    #     return values;
    # }
    def get_int_array(self):
        if self.INT_ARRAY != self.data[self.DATA_TYPE_OFFSET]:
            raise IllegalFieldAccessException()
        if self.data[self.DATA_OFFSET] < 0:
            return None
        values = [0] * ((len(self.data) - 2) // 4)
        buffer = BinaryDataBuffer(self.data)
        offset = self.DATA_OFFSET + 1
        for i in range(len(values)):
            values[i] = buffer.getInt(offset)
            offset += 4
        return values

    # /**
    #  * Get the long array contained with this field.
    #  * @return long array
    #  * @throws IllegalFieldAccessException if data type is not LONG_ARRAY.
    #  */
    # public long[] getLongArray() {
    #     if (LONG_ARRAY != data[DATA_TYPE_OFFSET]) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     if (data[DATA_OFFSET] < 0) {
    #         return null;
    #     }
    #     long[] values = new long[(data.length - 2) / 8];
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(data);
    #     int offset = DATA_OFFSET + 1;
    #     for (int i = 0; i < values.length; i++) {
    #         values[i] = buffer.getLong(offset);
    #         offset += 8;
    #     }
    #     return values;
    # }
    def get_long_array(self):
        if self.LONG_ARRAY != self.data[self.DATA_TYPE_OFFSET]:
            raise IllegalFieldAccessException()
        if self.data[self.DATA_OFFSET] < 0:
            return None
        values = [0] * ((len(self.data) - 2) // 8)
        buffer = BinaryDataBuffer(self.data)
        offset = self.DATA_OFFSET + 1
        for i in range(len(values)):
            values[i] = buffer.getLong(offset)
            offset += 8
        return values

    # /**
    #  * Get the float array contained with this field.
    #  * @return float array
    #  * @throws IllegalFieldAccessException if data type is not FLOAT_ARRAY.
    #  */
    # public float[] getFloatArray() {
    #     if (FLOAT_ARRAY != data[DATA_TYPE_OFFSET]) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     if (data[DATA_OFFSET] < 0) {
    #         return null;
    #     }
    #     float[] values = new float[(data.length - 2) / 4];
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(data);
    #     int offset = DATA_OFFSET + 1;
    #     for (int i = 0; i < values.length; i++) {
    #         values[i] = Float.intBitsToFloat(buffer.getInt(offset));
    #         offset += 4;
    #     }
    #     return values;
    # }
    def get_float_array(self):
        if self.FLOAT_ARRAY != self.data[self.DATA_TYPE_OFFSET]:
            raise IllegalFieldAccessException()
        if self.data[self.DATA_OFFSET] < 0:
            return None
        values = [0] * ((len(self.data) - 2) // 4)
        buffer = BinaryDataBuffer(self.data)
        offset = self.DATA_OFFSET + 1
        for i in range(len(values)):
            values[i] = Float.intBitsToFloat(buffer.getInt(offset))
            offset += 4
        return values

    # /**
    #  * Get the double array contained with this field.
    #  * @return double array
    #  * @throws IllegalFieldAccessException if data type is not DOUBLE_ARRAY.
    #  */
    # public double[] getDoubleArray() {
    #     if (DOUBLE_ARRAY != data[DATA_TYPE_OFFSET]) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     if (data[DATA_OFFSET] < 0) {
    #         return null;
    #     }
    #     double[] values = new double[(data.length - 2) / 8];
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(data);
    #     int offset = DATA_OFFSET + 1;
    #     for (int i = 0; i < values.length; i++) {
    #         values[i] = Double.longBitsToDouble(buffer.getLong(offset));
    #         offset += 8;
    #     }
    #     return values;
    # }
    def get_double_array(self):
        if self.DOUBLE_ARRAY != self.data[self.DATA_TYPE_OFFSET]:
            raise IllegalFieldAccessException()
        if self.data[self.DATA_OFFSET] < 0:
            return None
        values = [0] * ((len(self.data) - 2) // 8)
        buffer = BinaryDataBuffer(self.data)
        offset = self.DATA_OFFSET + 1
        for i in range(len(values)):
            values[i] = Double.longBitsToDouble(buffer.getLong(offset))
            offset += 8
        return values

    # /**
    #  * Get the String array contained with this field.
    #  * @return String array
    #  * @throws IllegalFieldAccessException if data type is not STRING_ARRAY.
    #  */
    # public String[] getStringArray() {
    #     if (STRING_ARRAY != data[DATA_TYPE_OFFSET]) {
    #         throw new IllegalFieldAccessException();
    #     }
    #     if (data[DATA_OFFSET] < 0) {
    #         return null;
    #     }
    #     ArrayList<String> strList = new ArrayList<String>();
    #     BinaryDataBuffer buffer = new BinaryDataBuffer(data);
    #     try {
    #         int offset = DATA_OFFSET + 1;
    #         while (offset < data.length) {
    #             int len = buffer.getInt(offset);
    #             offset += 4;
    #             if (len >= 0) {
    #                 byte[] bytes = buffer.get(offset, len);
    #                 strList.add(new String(bytes, STRING_ENCODING));
    #                 offset += len;
    #             }
    #             else {
    #                 strList.add(null);
    #             }
    #         }
    #     }
    #     catch (UnsupportedEncodingException e) {
    #         throw new AssertException();
    #     }
    #     String[] strings = new String[strList.size()];
    #     strList.toArray(strings);
    #     return strings;
    # }
    def get_string_array(self):
        if self.STRING_ARRAY != self.data[self.DATA_TYPE_OFFSET]:
            raise IllegalFieldAccessException()
        if self.data[self.DATA_OFFSET] < 0:
            return None
        strList = []
        buffer = BinaryDataBuffer(self.data)
        try:
            offset = self.DATA_OFFSET + 1
            while offset < len(self.data):
                len = buffer.getInt(offset)
                offset += 4
                if len >= 0:
                    bytes = buffer.get(offset, len)
                    strList.append(bytes.decode(self.STRING_ENCODING))
                    offset += len
                else:
                    strList.append(None)
        except UnsupportedEncodingException:
            raise AssertException()
        strings = [0] * len(strList)
        strList.copy(strings)
        return strings

# }
