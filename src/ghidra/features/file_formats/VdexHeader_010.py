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
package ghidra.file.formats.android.vdex.headers;

import java.io.IOException;

import ghidra.app.util.bin.BinaryReader;

# /**
 * <a href="https://android.googlesource.com/platform/art/+/refs/heads/oreo-m2-release/runtime/vdex_file.h#76">oreo-m2-release/runtime/vdex_file.h</a>
 * <br>
 * <a href="https://android.googlesource.com/platform/art/+/refs/heads/o-iot-preview-5/runtime/vdex_file.h#76">o-iot-preview-5/runtime/vdex_file.h</a>
 */
public class VdexHeader_010 extends VdexHeader_006 {
	public VdexHeader_010(BinaryReader reader) throws IOException {
		super(reader);
	}
}
