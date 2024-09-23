/* ###
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
package ghidra.file.formats.android.lz4;

import java.util.*;



import org.apache.commons.compress.compressors.lz4.BlockLZ4CompressorInputStream;

import ghidra.app.util.bin.BinaryReader;
import ghidra.app.util.bin.ByteProvider;
import ghidra.formats.gfilesystem.*;
import ghidra.formats.gfilesystem.annotations.FileSystemInfo;
import ghidra.formats.gfilesystem.factory.GFileSystemBaseFactory;
import ghidra.util.exception.CancelledException;
import ghidra.util.task.TaskMonitor;
import ghidra.util.task.UnknownProgressWrappingTaskMonitor;

/**
 * 
 * See: https://android.googlesource.com/platform/external/lz4/+/HEAD/doc/lz4_Frame_format.md
 *
 */
@FileSystemInfo(type = "lz4", description = "LZ4 Archive Format", factory = GFileSystemBaseFactory.class)
public class LZ4ArchiveFileSystem extends GFileSystemBase {

	/**
	 * LZ4 Magic Number
	 */
	public final static int ARCHIVE_MAGIC = 0x184C2102;
	public final static byte[] ARCHIVE_MAGIC_BYTES = { 0x02, 0x21, 0x4c, 0x18 };

	/**
	 * Note: Uncompressed chunk size is used in the compressor side
	 * (userspace side for compression).
	 * It is hardcoded because there is not proper way to extract it
	 * from the binary stream which is generated by the preliminary
	 * version of LZ4 tool so far.
	 */
	public final static int LZ4_DEFAULT_UNCOMPRESSED_CHUNK_SIZE = (8 << 20);

	public final static String NAME = "lz4_decompressed";

	private GFile decompressedLZ4File = null;

	public LZ4ArchiveFileSystem(String fileSystemName, ByteProvider provider) {
		super(fileSystemName, provider);
	}

	@Override
	public boolean isValid(TaskMonitor monitor) throws IOException {
		byte[] bytes = provider.readBytes(0, ARCHIVE_MAGIC_BYTES.length);
		return Arrays.equals(bytes, ARCHIVE_MAGIC_BYTES);
	}

	@Override
	public void open(TaskMonitor monitor) throws IOException, CancelledException {
		try (ByteProvider payloadBP = getPayload(monitor, root.getFSRL().appendPath(NAME))) {
			decompressedLZ4File =
				GFileImpl.fromFSRL(this, root, payloadBP.getFSRL(), false, payloadBP.length());
		}
	}

	private ByteProvider getPayload(TaskMonitor monitor, FSRL payloadFSRL)
			throws CancelledException, IOException {
		return fsService.getDerivedByteProviderPush(provider.getFSRL(), payloadFSRL, NAME, -1,
			os -> {
				BinaryReader reader = new BinaryReader(provider, true);//always LE
				int magic = reader.readNextInt();
				if (magic != ARCHIVE_MAGIC) {
					throw new IOException("LZ4 archive: invalid magic");
				}

				UnknownProgressWrappingTaskMonitor upwtm =
					new UnknownProgressWrappingTaskMonitor(monitor, provider.length());
				upwtm.setMessage("Decompressing LZ4 archive...");
				upwtm.setProgress(0);

				while (reader.hasNext()) {
					monitor.checkCancelled();

					int compressedChunkSize = reader.readNextInt();
					byte[] compressedChunk = reader.readNextByteArray(compressedChunkSize);
					try (InputStream compressedStream =
						new BlockLZ4CompressorInputStream(
							new ByteArrayInputStream(compressedChunk))) {
						long bytesCopied =
							FSUtilities.streamCopy(compressedStream, os, TaskMonitor.DUMMY);
						upwtm.incrementProgress(bytesCopied);
					}
				}
			}, monitor);
	}

	@Override
	public ByteProvider getByteProvider(GFile file, TaskMonitor monitor)
			throws IOException, CancelledException {
		if (file == decompressedLZ4File || file.equals(decompressedLZ4File)) {
			return getPayload(monitor, file.getFSRL());
		}
		return null;
	}

	@Override
	public List<GFile> getListing(GFile directory) throws IOException {
		return (directory == null || directory.equals(root)) && (decompressedLZ4File != null)
				? Arrays.asList(decompressedLZ4File)
				: Collections.emptyList();
	}
}
