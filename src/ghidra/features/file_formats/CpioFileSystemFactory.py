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
package ghidra.file.formats.cpio;

import java.io.IOException;

import org.apache.commons.compress.archivers.cpio.CpioArchiveInputStream;

import ghidra.app.util.bin.ByteProvider;
import ghidra.formats.gfilesystem.*;
import ghidra.formats.gfilesystem.factory.GFileSystemFactoryByteProvider;
import ghidra.formats.gfilesystem.factory.GFileSystemProbeBytesOnly;
import ghidra.util.exception.CancelledException;
import ghidra.util.task.TaskMonitor;

public class CpioFileSystemFactory
		implements GFileSystemFactoryByteProvider<CpioFileSystem>, GFileSystemProbeBytesOnly {

	@Override
	public CpioFileSystem create(FSRLRoot targetFSRL, ByteProvider byteProvider,
			FileSystemService fsService, TaskMonitor monitor)
			throws IOException, CancelledException {
		CpioFileSystem fs = new CpioFileSystem(targetFSRL, byteProvider, fsService, monitor);
		return fs;
	}

	@Override
	public int getBytesRequired() {
		return 6; // CpioArchiveInputStream doesn't have a value we can use, so we hard code
	}

	@Override
	public boolean probeStartBytes(FSRL containerFSRL, byte[] startBytes) {
		return CpioArchiveInputStream.matches(startBytes, startBytes.length);
	}
}
