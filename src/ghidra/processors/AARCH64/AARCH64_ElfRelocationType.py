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
package ghidra.app.util.bin.format.elf.relocation;

public enum AARCH64_ElfRelocationType implements ElfRelocationType {

	R_AARCH64_NONE(0),
	R_AARCH64_P32_ABS32(1),					// .word: (S+A)
	R_AARCH64_P32_ABS16(2),					// .half: (S+A)
	R_AARCH64_P32_PREL32(3),				// .word: (S+A-P) 
	R_AARCH64_P32_PREL16(4),				// .half: (S+A-P) 
	R_AARCH64_P32_MOVW_UABS_G0(5),			// MOV[ZK]: ((S+A) >>  0) & 0xffff 
	R_AARCH64_P32_MOVW_UABS_G0_NC(6),		// MOV[ZK]: ((S+A) >>  0) & 0xffff
	R_AARCH64_P32_MOVW_UABS_G1(7),			// MOV[ZK]: ((S+A) >> 16) & 0xffff
	R_AARCH64_P32_MOVW_SABS_G0(8),			// MOV[ZN]: ((S+A) >>  0) & 0xffff
	R_AARCH64_P32_LD_PREL_LO19(9),			// LD-lit: ((S+A-P) >> 2) & 0x7ffff
	R_AARCH64_P32_ADR_PREL_LO21(10),		// ADR: (S+A-P) & 0x1fffff
	R_AARCH64_P32_ADR_PREL_PG_HI21(11),		// ADRH: ((PG(S+A)-PG(P)) >> 12) & 0x1fffff
	R_AARCH64_P32_ADD_ABS_LO12_NC(12),		// ADD: (S+A) & 0xfff
	R_AARCH64_P32_LDST8_ABS_LO12_NC(13),	// LD/ST8: (S+A) & 0xfff
	R_AARCH64_P32_LDST16_ABS_LO12_NC(14),	// LD/ST16: (S+A) & 0xffe
	R_AARCH64_P32_LDST32_ABS_LO12_NC(15),	// LD/ST32: (S+A) & 0xffc
	R_AARCH64_P32_LDST64_ABS_LO12_NC(16),	// LD/ST64: (S+A) & 0xff8 
	R_AARCH64_P32_LDST128_ABS_LO12_NC(17),	// LD/ST128: (S+A) & 0xff0 
	R_AARCH64_P32_TSTBR14(18),				// TBZ/NZ: ((S+A-P) >> 2) & 0x3fff. 
	R_AARCH64_P32_CONDBR19(19),				// B.cond: ((S+A-P) >> 2) & 0x7ffff.
	R_AARCH64_P32_JUMP26(20),				// B:  ((S+A-P) >> 2) & 0x3ffffff.  
	R_AARCH64_P32_CALL26(21),				// BL: ((S+A-P) >> 2) & 0x3ffffff.

	R_AARCH64_P32_GOT_LD_PREL19(25),
	R_AARCH64_P32_ADR_GOT_PAGE(26),
	R_AARCH64_P32_LD32_GOT_LO12_NC(27),
	R_AARCH64_P32_LD32_GOTPAGE_LO14(28),

	R_AARCH64_P32_TLSGD_ADR_PREL21(80),
	R_AARCH64_P32_TLSGD_ADR_PAGE21(81),
	R_AARCH64_P32_TLSGD_ADD_LO12_NC(82),
	R_AARCH64_P32_TLSLD_ADR_PREL21(83),
	R_AARCH64_P32_TLSLD_ADR_PAGE21(84),
	R_AARCH64_P32_TLSLD_ADD_LO12_NC(85),
	R_AARCH64_P32_TLSLD_MOVW_DTPREL_G1(87),
	R_AARCH64_P32_TLSLD_MOVW_DTPREL_G0(88),
	R_AARCH64_P32_TLSLD_MOVW_DTPREL_G0_NC(89),
	R_AARCH64_P32_TLSLD_ADD_DTPREL_HI12(90),
	R_AARCH64_P32_TLSLD_ADD_DTPREL_LO12(91),
	R_AARCH64_P32_TLSLD_ADD_DTPREL_LO12_NC(92),
	R_AARCH64_P32_TLSIE_ADR_GOTTPREL_PAGE21(103),
	R_AARCH64_P32_TLSIE_LD32_GOTTPREL_LO12_NC(104),
	R_AARCH64_P32_TLSIE_LD_GOTTPREL_PREL19(105),
	R_AARCH64_P32_TLSLE_MOVW_TPREL_G1(106),
	R_AARCH64_P32_TLSLE_MOVW_TPREL_G0(107),
	R_AARCH64_P32_TLSLE_MOVW_TPREL_G0_NC(108),
	R_AARCH64_P32_TLSLE_ADD_TPREL_HI12(109),
	R_AARCH64_P32_TLSLE_ADD_TPREL_LO12(110),
	R_AARCH64_P32_TLSLE_ADD_TPREL_LO12_NC(111),
	R_AARCH64_P32_TLSLE_LDST8_TPREL_LO12(112),
	R_AARCH64_P32_TLSLE_LDST8_TPREL_LO12_NC(113),
	R_AARCH64_P32_TLSLE_LDST16_TPREL_LO12(114),
	R_AARCH64_P32_TLSLE_LDST16_TPREL_LO12_NC(115),
	R_AARCH64_P32_TLSLE_LDST32_TPREL_LO12(116),
	R_AARCH64_P32_TLSLE_LDST32_TPREL_LO12_NC(117),
	R_AARCH64_P32_TLSLE_LDST64_TPREL_LO12(118),
	R_AARCH64_P32_TLSLE_LDST64_TPREL_LO12_NC(119),

	R_AARCH64_P32_TLSDESC_LD_PREL19(122),
	R_AARCH64_P32_TLSDESC_ADR_PREL21(123),
	R_AARCH64_P32_TLSDESC_ADR_PAGE21(124),
	R_AARCH64_P32_TLSDESC_LD32_LO12_NC(125),
	R_AARCH64_P32_TLSDESC_ADD_LO12_NC(126),
	R_AARCH64_P32_TLSDESC_CALL(127),

	R_AARCH64_P32_COPY(180),			// Copy symbol at runtime.
	R_AARCH64_P32_GLOB_DAT(181),		// Create GOT entry.
	R_AARCH64_P32_JUMP_SLOT(182),		// Create PLT entry. 

	// Adjust by program base.  
	R_AARCH64_P32_RELATIVE(183),
	R_AARCH64_P32_TLS_DTPMOD(184),
	R_AARCH64_P32_TLS_DTPREL(185),
	R_AARCH64_P32_TLS_TPREL(186),
	R_AARCH64_P32_TLSDESC(187),
	R_AARCH64_P32_IRELATIVE(188),

	R_AARCH64_NULL(256), 				// No reloc 

	// Basic data relocations.  
	R_AARCH64_ABS64(257),				// .xword: (S+A)
	R_AARCH64_ABS32(258),				// .word:  (S+A)
	R_AARCH64_ABS16(259),				// .half: (S+A) 
	R_AARCH64_PREL64(260),				// .xword: (S+A-P)
	R_AARCH64_PREL32(261),				// .word: (S+A-P) 
	R_AARCH64_PREL16(262),				// .half:  (S+A-P)

	R_AARCH64_MOVW_UABS_G0(263),		// MOV[ZK]: ((S+A) >>  0) & 0xffff 
	R_AARCH64_MOVW_UABS_G0_NC(264),		// MOV[ZK]: ((S+A) >>  0) & 0xffff
	R_AARCH64_MOVW_UABS_G1(265),		// MOV[ZK]: ((S+A) >> 16) & 0xffff 
	R_AARCH64_MOVW_UABS_G1_NC(266),		// MOV[ZK]: ((S+A) >> 16) & 0xffff 
	R_AARCH64_MOVW_UABS_G2(267),		// MOV[ZK]: ((S+A) >> 32) & 0xffff 
	R_AARCH64_MOVW_UABS_G2_NC(268),		// MOV[ZK]: ((S+A) >> 32) & 0xffff 
	R_AARCH64_MOVW_UABS_G3(269),		// MOV[ZK]: ((S+A) >> 48) & 0xffff 
	R_AARCH64_MOVW_SABS_G0(270),		// MOV[ZN]: ((S+A) >>  0) & 0xffff 
	R_AARCH64_MOVW_SABS_G1(271),		// MOV[ZN]: ((S+A) >> 16) & 0xffff
	R_AARCH64_MOVW_SABS_G2(272),		// MOV[ZN]: ((S+A) >> 32) & 0xffff
	R_AARCH64_LD_PREL_LO19(273),		// LD-lit: ((S+A-P) >> 2) & 0x7ffff
	R_AARCH64_ADR_PREL_LO21(274),		// ADR:  (S+A-P) & 0x1fffff
	R_AARCH64_ADR_PREL_PG_HI21(275),	// ADRH: ((PG(S+A)-PG(P)) >> 12) & 0x1fffff 
	R_AARCH64_ADR_PREL_PG_HI21_NC(276),	// ADRH: ((PG(S+A)-PG(P)) >> 12) & 0x1fffff 
	R_AARCH64_ADD_ABS_LO12_NC(277),		// ADD:  (S+A) & 0xfff
	R_AARCH64_LDST8_ABS_LO12_NC(278),	// LD/ST8: (S+A) & 0xfff
	R_AARCH64_TSTBR14(279),				// TBZ/NZ: ((S+A-P) >> 2) & 0x3fff.
	R_AARCH64_CONDBR19(280),			// B.cond: ((S+A-P) >> 2) & 0x7ffff.
	R_AARCH64_JUMP26(282),				// B:  ((S+A-P) >> 2) & 0x3ffffff. 
	R_AARCH64_CALL26(283),				// BL: ((S+A-P) >> 2) & 0x3ffffff.
	R_AARCH64_LDST16_ABS_LO12_NC(284),	// LD/ST16: (S+A) & 0xffe
	R_AARCH64_LDST32_ABS_LO12_NC(285),	// LD/ST32: (S+A) & 0xffc
	R_AARCH64_LDST64_ABS_LO12_NC(286),	// LD/ST64: (S+A) & 0xff8
	R_AARCH64_MOVW_PREL_G0(287),
	R_AARCH64_MOVW_PREL_G0_NC(288),
	R_AARCH64_MOVW_PREL_G1(289),
	R_AARCH64_MOVW_PREL_G1_NC(290),
	R_AARCH64_MOVW_PREL_G2(291),
	R_AARCH64_MOVW_PREL_G2_NC(292),
	R_AARCH64_MOVW_PREL_G3(293),
	R_AARCH64_LDST128_ABS_LO12_NC(299),	// LD/ST128: (S+A) & 0xff0
	R_AARCH64_MOVW_GOTOFF_G0(300),
	R_AARCH64_MOVW_GOTOFF_G0_NC(301),
	R_AARCH64_MOVW_GOTOFF_G1(302),
	R_AARCH64_MOVW_GOTOFF_G1_NC(303),
	R_AARCH64_MOVW_GOTOFF_G2(304),
	R_AARCH64_MOVW_GOTOFF_G2_NC(305),
	R_AARCH64_MOVW_GOTOFF_G3(306),
	R_AARCH64_GOTREL64(307),
	R_AARCH64_GOTREL32(308),
	R_AARCH64_GOT_LD_PREL19(309),
	R_AARCH64_LD64_GOTOFF_LO15(310),
	R_AARCH64_ADR_GOT_PAGE(311),
	R_AARCH64_LD64_GOT_LO12_NC(312),
	R_AARCH64_LD64_GOTPAGE_LO15(313),

	R_AARCH64_TLSGD_ADR_PREL21(512),
	R_AARCH64_TLSGD_ADR_PAGE21(513),
	R_AARCH64_TLSGD_ADD_LO12_NC(514),
	R_AARCH64_TLSGD_MOVW_G1(515),
	R_AARCH64_TLSGD_MOVW_G0_NC(516),

	R_AARCH64_TLSLD_ADR_PREL21(517),
	R_AARCH64_TLSLD_ADR_PAGE21(518),
	R_AARCH64_TLSLD_ADD_LO12_NC(519),
	R_AARCH64_TLSLD_MOVW_G1(520),
	R_AARCH64_TLSLD_MOVW_G0_NC(521),
	R_AARCH64_TLSLD_LD_PREL19(522),
	R_AARCH64_TLSLD_MOVW_DTPREL_G2(523),
	R_AARCH64_TLSLD_MOVW_DTPREL_G1(524),
	R_AARCH64_TLSLD_MOVW_DTPREL_G1_NC(525),
	R_AARCH64_TLSLD_MOVW_DTPREL_G0(526),
	R_AARCH64_TLSLD_MOVW_DTPREL_G0_NC(527),
	R_AARCH64_TLSLD_ADD_DTPREL_HI12(528),
	R_AARCH64_TLSLD_ADD_DTPREL_LO12(529),
	R_AARCH64_TLSLD_ADD_DTPREL_LO12_NC(530),
	R_AARCH64_TLSLD_LDST8_DTPREL_LO12(531),
	R_AARCH64_TLSLD_LDST8_DTPREL_LO12_NC(532),
	R_AARCH64_TLSLD_LDST16_DTPREL_LO12(533),
	R_AARCH64_TLSLD_LDST16_DTPREL_LO12_NC(534),
	R_AARCH64_TLSLD_LDST32_DTPREL_LO12(535),
	R_AARCH64_TLSLD_LDST32_DTPREL_LO12_NC(536),
	R_AARCH64_TLSLD_LDST64_DTPREL_LO12(537),
	R_AARCH64_TLSLD_LDST64_DTPREL_LO12_NC(538),

	R_AARCH64_TLSIE_MOVW_GOTTPREL_G1(539),
	R_AARCH64_TLSIE_MOVW_GOTTPREL_G0_NC(540),
	R_AARCH64_TLSIE_ADR_GOTTPREL_PAGE21(541),
	R_AARCH64_TLSIE_LD64_GOTTPREL_LO12_NC(542),
	R_AARCH64_TLSIE_LD_GOTTPREL_PREL19(543),

	R_AARCH64_TLSLE_MOVW_TPREL_G2(544),
	R_AARCH64_TLSLE_MOVW_TPREL_G1(545),
	R_AARCH64_TLSLE_MOVW_TPREL_G1_NC(546),
	R_AARCH64_TLSLE_MOVW_TPREL_G0(547),
	R_AARCH64_TLSLE_MOVW_TPREL_G0_NC(548),
	R_AARCH64_TLSLE_ADD_TPREL_HI12(549),
	R_AARCH64_TLSLE_ADD_TPREL_LO12(550),
	R_AARCH64_TLSLE_ADD_TPREL_LO12_NC(551),
	R_AARCH64_TLSLE_LDST8_TPREL_LO12(552),
	R_AARCH64_TLSLE_LDST8_TPREL_LO12_NC(553),
	R_AARCH64_TLSLE_LDST16_TPREL_LO12(554),
	R_AARCH64_TLSLE_LDST16_TPREL_LO12_NC(555),
	R_AARCH64_TLSLE_LDST32_TPREL_LO12(556),
	R_AARCH64_TLSLE_LDST32_TPREL_LO12_NC(557),
	R_AARCH64_TLSLE_LDST64_TPREL_LO12(558),
	R_AARCH64_TLSLE_LDST64_TPREL_LO12_NC(559),

	R_AARCH64_TLSDESC_LD_PREL19(560),
	R_AARCH64_TLSDESC_ADR_PREL21(561),
	R_AARCH64_TLSDESC_ADR_PAGE21(562),
	R_AARCH64_TLSDESC_LD64_LO12_NC(563),
	R_AARCH64_TLSDESC_ADD_LO12_NC(564),
	R_AARCH64_TLSDESC_OFF_G1(565),
	R_AARCH64_TLSDESC_OFF_G0_NC(566),
	R_AARCH64_TLSDESC_LDR(567),
	R_AARCH64_TLSDESC_ADD(568),
	R_AARCH64_TLSDESC_CALL(569),

	R_AARCH64_TLSLE_LDST128_TPREL_LO12(570),
	R_AARCH64_TLSLE_LDST128_TPREL_LO12_NC(571),

	R_AARCH64_TLSLD_LDST128_DTPREL_LO12(572),
	R_AARCH64_TLSLD_LDST128_DTPREL_LO12_NC(573),

	R_AARCH64_COPY(1024),			// Copy symbol at runtime. 
	R_AARCH64_GLOB_DAT(1025),		// Create GOT entry.   
	R_AARCH64_JUMP_SLOT(1026),		// Create PLT entry.
	R_AARCH64_RELATIVE(1027),		// Adjust by program base.  
	R_AARCH64_TLS_DTPMOD64(1028),
	R_AARCH64_TLS_DTPREL64(1029),
	R_AARCH64_TLS_TPREL64(1030),
	R_AARCH64_TLS_DTPMOD(1028),
	R_AARCH64_TLS_DTPREL(1029),
	R_AARCH64_TLS_TPREL(1030),
	R_AARCH64_TLSDESC(1031),
	R_AARCH64_IRELATIVE(1032);

	public final int typeId;

	private AARCH64_ElfRelocationType(int typeId) {
		this.typeId = typeId;
	}

	@Override
	public int typeId() {
		return typeId;
	}
}
