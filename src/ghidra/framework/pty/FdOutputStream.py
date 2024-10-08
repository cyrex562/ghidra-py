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
package ghidra.pty.unix;


import java.io.OutputStream;

import com.sun.jna.LastErrorException;
import com.sun.jna.Memory;

# /**
 * An output stream that wraps a native POSIX file descriptor
 * 
 * <p>
 * <b>WARNING:</b> This class makes use of jnr-ffi to invoke native functions. An invalid file
 * descriptor is generally detected, but an incorrect, but valid file descriptor may cause undefined
 * behavior.
 */
public class FdOutputStream extends OutputStream {
	private static final PosixC LIB_POSIX = PosixC.INSTANCE;

	private final int fd;
	private boolean closed = false;

	/**
	 * Wrap the given file descriptor in an {@link OutputStream}
	 * 
	 * @param fd the file descriptor
	 */
	FdOutputStream(int fd) {
		this.fd = fd;
	}

	@Override
	public synchronized void write(int b) throws IOException {
		write(new byte[] { (byte) b });
	}

	@Override
	public synchronized void write(byte[] b) throws IOException {
		write(b, 0, b.length);
	}

	@Override
	public synchronized void write(byte[] b, int off, int len) throws IOException {
		if (closed) {
			throw new IOException("Stream closed");
		}
		Memory buf = new Memory(len);
		buf.write(0, b, off, len);
		try {
			int total = 0;
			do {
				int ret = LIB_POSIX.write(fd, buf, len - total);
				total += ret;
			}
			while (total < len);
		}
		catch (LastErrorException e) {
			if (e.getErrorCode() == 5 || e.getErrorCode() == 9) {
				throw new IOException(e);
			}
			throw e;
		}
	}

	@Override
	public synchronized void close() throws IOException {
		closed = true;
	}
}
