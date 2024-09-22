# /* ###
 * IP: GHIDRA
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package docking.widgets.table.constraint.provider;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Date;

import docking.widgets.table.constraint.ColumnTypeMapper;

# /**
 * Converts Date Column objects to LocalDate objects so that column gets LocalDate type column
 * filters
 */
public class DateColumnTypeMapper extends ColumnTypeMapper<Date, LocalDate> {

	@Override
	public LocalDate convert(Date value) {
		return value.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
	}
}
