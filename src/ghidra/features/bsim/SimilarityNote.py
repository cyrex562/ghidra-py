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
package ghidra.features.bsim.query.protocol;


import java.io.Writer;
import java.util.Map;

import ghidra.features.bsim.query.LSHException;
import ghidra.features.bsim.query.description.*;
import ghidra.util.xml.SpecXmlUtils;
import ghidra.xml.XmlElement;
import ghidra.xml.XmlPullParser;

# /**
 * A description of a single function match
 *
 */
public class SimilarityNote implements Comparable<SimilarityNote> {
	private FunctionDescription func;		// Description of function that was matched
	private double sim;		// Similarity of the match
	private double signif;	// Significance of the match
	
	public SimilarityNote() {}		// For use with restoreXml
	
	public SimilarityNote(FunctionDescription f,double sm,double sf) {
		func = f;
		sim = sm;
		signif = sf;
	}
	
	public FunctionDescription getFunctionDescription() { return func; }
	
	public double getSimilarity() { return sim; }
	
	public double getSignificance() { return signif; }

	public void transfer(DescriptionManager manage,boolean transsig) throws LSHException {
		func = manage.transferFunction(func,transsig);
	}

	public void setTransfer(SimilarityNote op2,DescriptionManager manage,boolean transsig) throws LSHException {
		func = manage.transferFunction(op2.func, transsig);
		sim = op2.sim;
		signif = op2.signif;
	}

	public void saveXml(Writer write) throws IOException {
		StringBuilder buf = new StringBuilder();
		buf.append("<note");
		SpecXmlUtils.encodeUnsignedIntegerAttribute(buf, "id", func.getExecutableRecord().getXrefIndex());
		SpecXmlUtils.xmlEscapeAttribute(buf, "name", func.getFunctionName());
		SpecXmlUtils.encodeUnsignedIntegerAttribute(buf, "addr", func.getAddress());
		buf.append(">\n");
		buf.append(" <sim>").append(Double.toString(sim)).append("</sim>\n");
		buf.append(" <sig>").append(Double.toString(signif)).append("</sig>\n");
		buf.append("</note>\n");
		write.append(buf.toString());
	}
	
	public void restoreXml(XmlPullParser parser,DescriptionManager manage, Map<Integer,ExecutableRecord> exeMap) throws LSHException {
		XmlElement el = parser.start("note");
		int id = SpecXmlUtils.decodeInt(el.getAttribute("id"));
		ExecutableRecord exe = exeMap.get(id);
		long address = SpecXmlUtils.decodeLong(el.getAttribute("addr"));
		func = manage.findFunction(el.getAttribute("name"), address, exe);
		parser.start("sim");
		sim = Double.parseDouble(parser.end().getText());
		parser.start("sig");
		signif = Double.parseDouble(parser.end().getText());
		parser.end();
	}

	@Override
	public int compareTo(SimilarityNote o) {
		return func.compareTo(o.func);
	}
}
