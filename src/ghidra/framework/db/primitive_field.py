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

from .field import Field


# /**
#  * <code>PrimitiveField</code> provides a base implementation for
#  * all primitive value {@link Field}s.
#  * <br>
#  * When a {@link PrimitiveField} associated with a {@link SparseRecord}
#  * has a null state it will have a zero (0) value.
#  */
# abstract class PrimitiveField extends Field {
class PrimitiveField(Field, ABC):

    # private boolean isNull = false;

    # /**
    #  * Abstract PrimitiveField Constructor for a mutable instance
    #  */
    # PrimitiveField() {
    # 	super();
    # }
    def __init__(
        self,
        immutable: bool | None = None,
    ):
        super().__init__()
        self.isNull = False
        if immutable is not None:
            self.immutable = immutable

    # /**
    #  * Abstract PrimitiveField Constructor
    #  * @param immutable true if field value is immutable
    #  */
    # PrimitiveField(boolean immutable) {
    # 	super(immutable);
    # }

    # @Override
    # public final boolean isNull() {
    #     return isNull;
    # }
    @property
    def isNull(self) -> bool:
        return self._isNull

    @isNull.setter
    def isNull(self, isNull: bool) -> None:
        self._isNull = isNull

    # @Override
    # void setNull() {
    #     checkImmutable();
    #     this.isNull = true;
    # }
    def setNull(self) -> None:
        self.checkImmutable()
        self.isNull = True

    # /**
    #  * Invoked prior to setting the field's primitive value this
    #  * method will perform an immutable check and set to a non-null
    #  * state.
    #  */
    # final void updatingPrimitiveValue() {
    #     checkImmutable();
    #     this.isNull = false;
    # }
    def updatingPrimitiveValue(self) -> None:
        self.checkImmutable()
        self.isNull = False

    # @Override
    # public String toString() {
    #     String nullState = "";
    #     if (isNull()) {
    #         nullState = "(NULL)";
    #     }
    #     return getClass().getSimpleName() + nullState + ": " + getValueAsString();
    # }
    def __str__(self) -> str:
        nullState = ""
        if self.isNull:
            nullState = "(NULL)"
        return f"{self.__class__.__name__}{nullState}: {self.getValueAsString()}"


# }
