import unittest
from spdx_expression_paths import choices
class Contract(unittest.TestCase):
    def test_atom(self):self.assertEqual(choices('MIT')['alternatives'],[['MIT']])
    def test_or(self):self.assertEqual(choices('MIT OR Apache-2.0')['alternatives'],[['Apache-2.0'],['MIT']])
    def test_and(self):self.assertEqual(choices('MIT AND Apache-2.0')['alternatives'],[['Apache-2.0','MIT']])
    def test_precedence(self):self.assertEqual(choices('MIT OR Apache-2.0 AND BSD-3-Clause')['alternatives'],[['Apache-2.0','BSD-3-Clause'],['MIT']])
    def test_distribution(self):self.assertEqual(choices('(MIT OR BSD-2-Clause) AND Zlib')['alternatives'],[['BSD-2-Clause','Zlib'],['MIT','Zlib']])
    def test_with_atomic(self):self.assertEqual(choices('GPL-2.0-only WITH Classpath-exception-2.0 OR MIT')['alternatives'],[['GPL-2.0-only WITH Classpath-exception-2.0'],['MIT']])
    def test_duplicate_paths(self):self.assertEqual(choices('MIT OR MIT')['count'],1)
    def test_duplicate_terms(self):self.assertEqual(choices('MIT AND MIT')['alternatives'],[['MIT']])
    def test_license_ref(self):self.assertEqual(choices('LicenseRef-Local+')['count'],1)
    def test_limit(self):
        with self.assertRaises(ValueError):choices('MIT OR Zlib',1)
    def test_unknown_id_explicit(self):self.assertIn('not registry-validated',choices('Not-A-License')['scope'])
    def test_invalid(self):
        for s in ('','MIT AND','(MIT','MIT)','MIT WITH','MIT && Zlib','MIT Zlib','WITH MIT','MIT WITH (Zlib)','(MIT OR Zlib) WITH Exception'):
            with self.subTest(s=s),self.assertRaises(ValueError):choices(s)
    def test_depth_limit(self):
        with self.assertRaises(ValueError):choices('('*34+'MIT'+')'*34)
    def test_work_limit(self):
        with self.assertRaises(ValueError):choices(' AND '.join('(A%d OR B%d)'%(i,i) for i in range(11)),1024)
    def test_invalid_limit(self):
        with self.assertRaises(ValueError):choices('MIT',True)
    def test_whitespace(self):self.assertEqual(choices('  MIT \n OR\t Zlib  ')['count'],2)
