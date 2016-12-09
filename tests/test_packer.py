from unittest import TestCase
from rectpack.geometry import Rectangle
import rectpack.skyline as skyline
import rectpack.guillotine as guillotine
import rectpack.packer as packer


class TestRectangleSort(TestCase):

    def test_sort_none(self):
        """Test list is returned a is"""
        a = [(3, 3), (3, 1), (3, 2), (1, 2), (2, 1)]
        ordered = packer.SORT_NONE(a)
        self.assertEqual(a, ordered)
            
        # Test empty list
        self.assertEqual(packer.SORT_NONE([]), [])

    def test_sort_area(self):
        """Test rectangles are sorted by descending area"""
        a = [(5, 5), (7, 7), (3, 4), (100, 1)]
        ordered = packer.SORT_AREA(a)
        self.assertEqual(ordered, [(100, 1), (7, 7), (5, 5), (3, 4)])
        
        # Test empty list
        self.assertEqual(packer.SORT_AREA([]), [])

    def test_sort_peri(self):
        """Test rectangles are sorted by perimeter"""
        a = [(5, 5), (7, 7), (3, 4), (40, 1)]
        ordered = packer.SORT_PERI(a)
        self.assertEqual(ordered, [(40, 1), (7, 7), (5, 5), (3, 4)])

        # Test empty list
        self.assertEqual(packer.SORT_PERI([]), [])

    def test_sort_diff(self):
        """Test rectangles are sorted by the difference in side lengths"""
        a = [(7, 1), (1, 9), (2, 11), (5, 1)]
        ordered = packer.SORT_DIFF(a)
        self.assertEqual(ordered, [(2, 11), (1, 9), (7, 1), (5, 1)])

        # Test empty list
        self.assertEqual(packer.SORT_DIFF([]), [])

    def test_sort_sside(self):
        """Test rectangles are sorted by short side descending"""
        a = [(2, 9), (7, 3), (4, 5), (11, 3)]
        ordered = packer.SORT_SSIDE(a)
        self.assertEqual(ordered, [(4, 5), (11, 3), (7, 3), (2, 9)])

        # Test empty list
        self.assertEqual(packer.SORT_SSIDE([]), [])

    def test_sort_lside(self):
        """Test rectangles are sorted by long side descending"""
        a = [(19, 5), (32, 5), (6, 19), (9, 11)]
        ordered = packer.SORT_LSIDE(a)
        self.assertEqual(ordered, [(32, 5), (6, 19), (19, 5), (9, 11)])

        # Test empty list
        self.assertEqual(packer.SORT_LSIDE([]), [])

    def test_sort_ratio(self):
        """Test rectangles are sorted by width/height descending"""
        a = [(12, 5), (15, 4), (4, 1), (1, 2)]
        ordered = packer.SORT_RATIO(a)
        self.assertEqual(ordered, [(4, 1), (15, 4), (12, 5), (1, 2)])

        # Test empty list
        self.assertEqual(packer.SORT_RATIO([]), [])



class TestPackerOnline(TestCase):

    def test_getitem_bnf(self):
        """Test getitem  and len"""
        p = packer.PackerOnlineBNF(rotation=False)
        p.add_bin(50, 55)
        p.add_bin(30, 30)
        p.add_bin(40, 40)
        with self.assertRaises(IndexError):
            p[0]

        # Rect 1
        p.add_rect(50, 50)
        with self.assertRaises(IndexError):
            p[1]
        with self.assertRaises(IndexError):
            p[-2]
        self.assertEqual(len(p), 1)
        self.assertEqual(p[0].width, 50)
        self.assertEqual(p[0].height, 55)
        self.assertEqual(p[-1].width, 50)
        self.assertEqual(p[-1].height, 55)

        # Rect 2
        p.add_rect(40, 40)
        with self.assertRaises(IndexError):
            p[3]
        with self.assertRaises(IndexError):
            p[-4]
        self.assertEqual(len(p), 3)
        self.assertEqual(p[0].width, 50)
        self.assertEqual(p[0].height, 55)
        self.assertEqual(p[1].width, 30)
        self.assertEqual(p[1].height, 30)
        self.assertEqual(p[2].width, 40)
        self.assertEqual(p[2].height, 40)
        self.assertEqual(p[-1].width, 40)
        self.assertEqual(p[-1].height, 40)
        self.assertEqual(p[-2].width, 30)
        self.assertEqual(p[-2].height, 30)
        self.assertEqual(p[-3].width, 50)
        self.assertEqual(p[-3].height, 55)

    def test_getitem_bff(self):
        """Test more getitem and len"""
        p = packer.PackerOnlineBFF(rotation=False)
        p.add_bin(50, 55)
        p.add_bin(30, 30)
        p.add_bin(40, 40)
        with self.assertRaises(IndexError):
            p[0]

        # Rect 1
        p.add_rect(50, 50)
        with self.assertRaises(IndexError):
            p[1]
        with self.assertRaises(IndexError):
            p[-2]
        self.assertEqual(len(p), 1)
        self.assertEqual(p[0].width, 50)
        self.assertEqual(p[0].height, 55)
        self.assertEqual(p[-1].width, 50)
        self.assertEqual(p[-1].height, 55)

        # Rect 2
        p.add_rect(40, 40)
        with self.assertRaises(IndexError):
            p[3]
        with self.assertRaises(IndexError):
            p[-4]
        self.assertEqual(len(p), 3)
        self.assertEqual(p[0].width, 50)
        self.assertEqual(p[0].height, 55)
        self.assertEqual(p[1].width, 30)
        self.assertEqual(p[1].height, 30)
        self.assertEqual(p[2].width, 40)
        self.assertEqual(p[2].height, 40)
        self.assertEqual(p[-1].width, 40)
        self.assertEqual(p[-1].height, 40)
        self.assertEqual(p[-2].width, 30)
        self.assertEqual(p[-2].height, 30)
        self.assertEqual(p[-3].width, 50)
        self.assertEqual(p[-3].height, 55)

    def test_getitem_bbf(self):
        """And more getitem and len tests"""
        p = packer.PackerOnlineBFF(rotation=False)
        p.add_bin(50, 55)
        p.add_bin(30, 30)
        p.add_bin(40, 40)
        with self.assertRaises(IndexError):
            p[0]

        # Rect 1
        p.add_rect(50, 50)
        with self.assertRaises(IndexError):
            p[1]
        with self.assertRaises(IndexError):
            p[-2]
        self.assertEqual(len(p), 1)
        self.assertEqual(p[0].width, 50)
        self.assertEqual(p[0].height, 55)
        self.assertEqual(p[-1].width, 50)
        self.assertEqual(p[-1].height, 55)

        # Rect 2
        p.add_rect(40, 40)
        with self.assertRaises(IndexError):
            p[3]
        with self.assertRaises(IndexError):
            p[-4]
        self.assertEqual(len(p), 3)
        self.assertEqual(p[0].width, 50)
        self.assertEqual(p[0].height, 55)
        self.assertEqual(p[1].width, 30)
        self.assertEqual(p[1].height, 30)
        self.assertEqual(p[2].width, 40)
        self.assertEqual(p[2].height, 40)
        self.assertEqual(p[-1].width, 40)
        self.assertEqual(p[-1].height, 40)
        self.assertEqual(p[-2].width, 30)
        self.assertEqual(p[-2].height, 30)
        self.assertEqual(p[-3].width, 50)
        self.assertEqual(p[-3].height, 55)



    
class TestPackerOnlineBNF(TestCase):

    def test_packing(self):
        p = packer.PackerOnlineBNF()
        p.add_bin(30, 30)
        p.add_bin(40, 40)
        p.add_rect(40, 40)
        self.assertEqual(p.rect_list()[0], (1, 0, 0, 40, 40, None))

    def test_rotation(self):
        p = packer.PackerOnlineBNF(rotation=False)
        p.add_bin(30, 10)
        p.add_bin(50, 10)
        p.add_rect(10, 30)
        self.assertEqual(len(p.rect_list()), 0)
        self.assertEqual(len(p), 2)

        p = packer.PackerOnlineBNF(rotation=True)
        p.add_bin(30, 10)
        p.add_bin(50, 10)
        p.add_rect(10, 30)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 30, 10, None))
        self.assertEqual(len(p), 1)



class TestPackerOnlineBFF(TestCase):
    
    def test_packing(self):
        p = packer.PackerOnlineBFF(pack_algo=guillotine.GuillotineBafSas, 
                rotation=False)

        p.add_bin(20, 20)
        p.add_bin(100, 100)

        p.add_rect(10, 10)
        p.add_rect(90, 90)
        p.add_rect(10, 10)
        self.assertEqual(len(p.rect_list()), 3)
        self.assertTrue((0, 0, 0, 10, 10, None) in p.rect_list())
        self.assertTrue((1, 0, 0, 90, 90, None) in p.rect_list())
        self.assertTrue((0, 0, 10, 10, 10, None) in p.rect_list())

        # Test bin order
        p = packer.PackerOnlineBFF(pack_algo=guillotine.GuillotineBafSas, 
                rotation=False)

        p.add_bin(20, 20)
        p.add_bin(100, 100)

        p.add_rect(90, 90)
        p.add_rect(10, 10)
        p.add_rect(10, 10)
        self.assertEqual(len(p.rect_list()), 3)
        self.assertTrue((0, 0, 0, 10, 10, None) in p.rect_list())
        self.assertTrue((1, 0, 0, 90, 90, None) in p.rect_list())
        self.assertTrue((0, 0, 10, 10, 10, None) in p.rect_list())

        # Test empty bins
        p = packer.PackerOnlineBFF(pack_algo=guillotine.GuillotineBafSas, 
                rotation=False)

        p.add_bin(20, 20)
        p.add_bin(100, 100)

        p.add_rect(90, 90)
        self.assertEqual(len(p.rect_list()), 1)
        self.assertTrue((1, 0, 0, 90, 90, None) in p.rect_list())
        self.assertEqual(len(p.bin_list()), 2)


class TestPackerOnlineBBF(TestCase):

    def test_pack(self):
        """Test bin with best fitness is selected"""
        p = packer.PackerOnlineBBF(pack_algo=guillotine.GuillotineBafSas, 
                rotation=False)
      
        p.add_bin(10, 10)
        p.add_bin(15, 15)
        p.add_bin(55, 55)
        p.add_bin(50, 50)
        p.add_rect(50, 30)
        p.add_rect(50, 30)
        p.add_rect(20, 20)
        p.add_rect(10, 10)

        self.assertEqual(len(p.rect_list()), 4)
        self.assertEqual(len(p), 4)
        self.assertTrue((2, 0, 0, 50, 30, None) in p.rect_list())
        self.assertTrue((3, 0, 0, 50, 30, None) in p.rect_list())
        self.assertTrue((3, 0, 30, 20, 20, None) in p.rect_list())
        self.assertTrue((0, 0, 0, 10, 10, None) in p.rect_list())


class TestPacker(TestCase):

    def test_init(self):
        # Test rotation is enabled by default
        p = packer.PackerBNF(rotation=True)
        p.add_bin(100, 10)
        p.add_rect(10, 89)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 89, 10, None))

        # Test default packing algo
        p = packer.PackerBFF()
        p.add_bin(10, 10)
        p.add_rect(1, 1)
        p.pack()
        for b in p:
            self.assertIsInstance(b, skyline.SkylineBlWm)
        
        # Test default sorting algo is unsorted
        p = packer.PackerBFF(pack_algo=guillotine.GuillotineBssfSas, rotation=False)
        self.assertEqual(p._sort_algo, packer.SORT_LSIDE)
        
        #
        p = packer.PackerBFF(pack_algo=guillotine.GuillotineBssfSas, 
                sort_algo=packer.SORT_NONE, rotation=False)
        p.add_bin(100, 100)
        p.add_rect(1, 4)
        p.add_rect(4, 4)
        p.add_rect(1, 8)
        p.pack()
        self.assertEqual(p.rect_list()[0][3], 1) # width
        self.assertEqual(p.rect_list()[0][4], 4) # height
        self.assertEqual(p.rect_list()[1][3], 4) # width
        self.assertEqual(p.rect_list()[1][4], 4) # height
        self.assertEqual(p.rect_list()[2][3], 1) # width
        self.assertEqual(p.rect_list()[2][4], 8) # height

        # Test custom packing algo is stored and used
        p = packer.PackerBFF(pack_algo=guillotine.GuillotineBafSas)
        p.add_bin(10, 10)
        p.add_rect(1, 1)
        p.pack()
        for b in p:
            self.assertIsInstance(b, guillotine.GuillotineBafSas)

        # Test custom sorting algo is stored and used
        p = packer.PackerBFF(sort_algo=packer.SORT_AREA, 
                pack_algo=skyline.SkylineBl, rotation=False)
        p.add_bin(100, 100)
        p.add_rect(1, 1)
        p.add_rect(4, 5)
        p.add_rect(0.5, 0.1)
        p.add_rect(2, 3)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 4, 5, None))
        self.assertEqual(p.rect_list()[1], (0, 4, 0, 2, 3, None))
        self.assertEqual(p.rect_list()[2], (0, 6, 0, 1, 1, None))
        self.assertEqual(p.rect_list()[3], (0, 7, 0, 0.5, 0.1, None))

        # Test rotation is stored and passed to algos
        p = packer.PackerBFF(sort_algo=packer.SORT_AREA, 
                pack_algo=skyline.SkylineBl, rotation=False)
        p.add_bin(100, 100)
        p.add_rect(1, 20)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 1, 20, None))

        p = packer.PackerBFF(sort_algo=packer.SORT_AREA, 
                pack_algo=skyline.SkylineBl, rotation=True)
        p.add_bin(100, 100)
        p.add_rect(1, 20)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 1, None))

    def test_iter(self):
        p = packer.PackerBFF()
        p.add_bin(100, 100)
        p.add_rect(1, 1)
        p.pack()
        bins = [b for b in p]
        self.assertEqual(len(bins), 1)

    def test_rectangles_sorted(self):
        """Test rectangles are sorted before packing"""
        p = packer.PackerBFF(sort_algo=packer.SORT_AREA)
        p.add_bin(30, 30)
        p.add_rect(20, 20)
        p.add_rect(25, 25)
        p.pack()
       
        # Test the bigger rectangle is placed first
        for b in p:
            for r in b:
                self.assertEqual(r, Rectangle(0, 0, 25, 25, None))

    def test_multiple_bins(self):
        """Test rectangles are placed into several bins"""
        p = packer.PackerBFF(sort_algo=packer.SORT_NONE)
        p.add_bin(30, 30)
        p.add_bin(40, 40)
        p.add_rect(25, 25)
        p.add_rect(30, 30)
        p.pack()

        self.assertEqual(p.rect_list()[0], (0, 0, 0, 25, 25, None))
        self.assertEqual(p.rect_list()[1], (1, 0, 0, 30, 30, None))

        # Doesn't fit first bin
        p = packer.PackerBFF(sort_algo=packer.SORT_NONE)
        p.add_bin(25, 25)
        p.add_bin(40, 40)
        p.add_rect(30, 30)
        p.add_rect(25, 25)
        p.pack()

        self.assertEqual(p.rect_list()[0], (0, 0, 0, 25, 25, None))
        self.assertEqual(p.rect_list()[1], (1, 0, 0, 30, 30, None))

    def test_rotation(self):
        """Test rotation is enabled by default and can be disabled"""
        p = packer.PackerBFF(sort_algo=packer.SORT_NONE)
        p.add_bin(10, 50)
        p.add_rect(50, 10)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 10, 50, None))

        p = packer.PackerBFF(rotation=False)
        p.add_bin(10, 50)
        p.add_rect(50, 10)
        p.pack()
        self.assertEqual(p.rect_list(), [])

    def test_pack(self):

        # Without bins
        p = packer.PackerBFF()
        p.add_rect(10, 10)
        p.pack()

        self.assertEqual(p.rect_list(), [])
        self.assertEqual(p.bin_list(), [])

        # Without rectangles
        p = packer.PackerBFF()
        p.add_bin(10, 10)
        p.pack()
        self.assertEqual(p.rect_list(), [])
        self.assertEqual(p.bin_list(), [])

        # Test packing using several bins
        p = packer.PackerBFF()
        p.add_bin(20, 10)
        p.add_bin(50, 50)
        p.add_rect(30, 30)
        p.add_rect(10, 20)
        p.pack()

        self.assertEqual(len(p.bin_list()), 2)
        self.assertEqual(p.rect_list()[1], (1, 0, 0, 30, 30, None))
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 10, None))

        # Test empty bins not returned
        p = packer.PackerBFF()
        p.add_rect(5, 5)
        p.add_rect(6, 6)
        p.add_bin(20, 20)
        p.add_bin(30, 30)
        p.add_bin(10, 10)
        p.pack()

        self.assertEqual(len(p.bin_list()), 1)
        self.assertEqual(len(p.rect_list()), 2)

        # Test rectangles too big
        p = packer.PackerBFF()
        p.add_bin(30, 30)
        p.add_rect(40, 50)
        p.pack()
        self.assertEqual(len(p.bin_list()), 1)
        self.assertEqual(len(p.rect_list()), 0)

        # Test state before calling pack
        p = packer.PackerBFF()
        p.add_bin(10, 10)
        p.add_rect(3, 3)

        self.assertEqual(len(p.bin_list()), 0)
        self.assertEqual(len(p.rect_list()), 0)
   
        # Test repacking after adding more rectangles and bins
        p = packer.PackerBFF(sort_algo=packer.SORT_NONE)
        p.add_bin(100, 100)
        p.add_rect(3, 3)
        p.pack()

        self.assertEqual(len(p.bin_list()), 1)
        self.assertEqual(len(p.rect_list()), 1)

        p.add_rect(10, 10)
        p.add_rect(120, 100)
        p.add_bin(200, 200)
        p.pack()
        
        self.assertEqual(len(p.bin_list()), 2)
        self.assertEqual(len(p.rect_list()), 3)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 3, 3, None))
        self.assertEqual(p.rect_list()[1], (0, 3, 0, 10, 10, None))
        self.assertEqual(p.rect_list()[2], (1, 0, 0, 120, 100, None))
        self.assertEqual(p.bin_list()[0], (100, 100))
        self.assertEqual(p.bin_list()[1], (200, 200))

    def test_repack(self):
        """Test can be repacked after adding a rectangle or bin"""
        p = packer.PackerBFF(rotation=False)
        p.add_bin(50, 50)
        p.add_rect(20, 20)
        p.pack()

        self.assertEqual(len(p.rect_list()), 1)
        self.assertEqual(len(p.bin_list()), 1)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))
        
        # Add more rectangles and re-pack
        p.add_rect(10, 10)
        p.add_rect(70, 50)
        p.pack()
        self.assertEqual(len(p.rect_list()), 2)
        self.assertEqual(len(p.bin_list()), 1)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))
        self.assertEqual(p.rect_list()[1], (0, 20, 0, 10, 10, None))

        # Add more bins and re-pack
        p.add_bin(70, 70)
        p.add_bin(100, 100)
        p.pack()
        self.assertEqual(len(p.rect_list()), 3)
        self.assertEqual(len(p.bin_list()), 2)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))
        self.assertEqual(p.rect_list()[1], (0, 20, 0, 10, 10, None))
        self.assertEqual(p.rect_list()[2], (1, 0, 0, 70, 50, None))


class TestPackerBNF(TestCase):
    
    def test_bin_closing(self):
        """Test bins are closed after one failed packing attempt"""
        p = packer.PackerBNF(pack_algo=guillotine.GuillotineBafSas, 
                sort_algo=packer.SORT_NONE, rotation=False)
        p.add_bin(50, 50)
        p.add_bin(100, 100)
        p.add_bin(300, 300)
        p.add_rect(40, 40)
        p.add_rect(90, 90)
        p.add_rect(5, 5)
        p.add_rect(20, 20)
        p.add_rect(10, 10)
        p.pack()
        
        packing = [(0, 0, 0, 40, 40, None), 
                (1, 0, 0, 90, 90, None), 
                (1, 0, 90, 5, 5, None), 
                (2, 0, 0, 20, 20, None),
                (2, 0, 20, 10, 10, None)]
        self.assertEqual(packing, p.rect_list())
 
    def test_repack(self):
        """Test can be packed a second time"""
        p = packer.PackerBNF(pack_algo=guillotine.GuillotineBafSas,
                sort_algo=packer.SORT_NONE, rotation=False)
        p.add_bin(100, 100)
        p.add_rect(20, 20)
        p.pack()
        
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))

        # Add rectangles and repack
        p.add_rect(80, 80)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))
        self.assertEqual(p.rect_list()[1], (0, 20, 0, 80, 80, None))
 
    def test_repack_sorted(self):
        """Test can be packed a second time sorted"""
        p = packer.PackerBNF(pack_algo=guillotine.GuillotineBafSas,
                sort_algo=packer.SORT_LSIDE, rotation=False)
        p.add_bin(100, 100)
        p.add_rect(20, 20)
        p.pack()
        
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))

        # Add rectangles and repack
        p.add_rect(80, 80)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 80, 80, None))
        self.assertEqual(p.rect_list()[1], (0, 0, 80, 20, 20, None))


    

class TestPackerBFF(TestCase):
    
    def test_first_packing(self):
        """Test rectangles are packed into the first bin with enough space"""
        p = packer.PackerBFF(pack_algo=guillotine.GuillotineBafSas,
                sort_algo=packer.SORT_NONE, rotation=False)
        p.add_bin(50, 50)
        p.add_bin(50, 100)
        p.add_rect(50, 20)
        p.add_rect(50, 80)
        p.add_rect(50, 20)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 50, 20, None))
        self.assertEqual(p.rect_list()[1], (0, 0, 20, 50, 20, None))
        self.assertEqual(p.rect_list()[2], (1, 0, 0, 50, 80, None))
        self.assertEqual(p.bin_list()[0], (50, 50))
        self.assertEqual(p.bin_list()[1], (50, 100))
        
        # Compare bin selection with BBF
        p = packer.PackerBBF(pack_algo=guillotine.GuillotineBafSas,
                sort_algo=packer.SORT_NONE, rotation=False)
        p.add_bin(50, 50)
        p.add_bin(50, 100)
        p.add_rect(50, 20)
        p.add_rect(50, 80)
        p.add_rect(50, 20)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 50, 20, None))
        self.assertEqual(p.rect_list()[1], (1, 0, 0, 50, 80, None))
        self.assertEqual(p.rect_list()[2], (1, 0, 80, 50, 20, None))
        self.assertEqual(p.bin_list()[0], (50, 50))
        self.assertEqual(p.bin_list()[1], (50, 100))
 
    def test_repack(self):
        """Test can be packed a second time"""
        p = packer.PackerBFF(pack_algo=guillotine.GuillotineBafSas,
                sort_algo=packer.SORT_NONE, rotation=False)
        p.add_bin(100, 100)
        p.add_rect(20, 20)
        p.pack()
        
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))

        # Add rectangles and repack
        p.add_rect(80, 80)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))
        self.assertEqual(p.rect_list()[1], (0, 20, 0, 80, 80, None))
 
    def test_repack_sorted(self):
        """Test can be packed a second time sorted"""
        p = packer.PackerBFF(pack_algo=guillotine.GuillotineBafSas,
                sort_algo=packer.SORT_LSIDE, rotation=False)
        p.add_bin(100, 100)
        p.add_rect(20, 20)
        p.pack()
        
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))

        # Add rectangles and repack
        p.add_rect(80, 80)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 80, 80, None))
        self.assertEqual(p.rect_list()[1], (0, 0, 80, 20, 20, None))




class TestPackerBBF(TestCase):
    """BBF (Bin Best Fit): Pack rectangle in bin that gives best fitness"""
    def test_best_fit(self):
        p = packer.PackerBBF(pack_algo=guillotine.GuillotineBafSas,
                sort_algo=packer.SORT_NONE, rotation=False)
        p.add_bin(50, 50)
        p.add_bin(50, 60)
        p.add_rect(50, 20)
        p.add_rect(50, 40)
        p.add_rect(50, 20)
        p.pack()
        self.assertEqual(p.bin_list()[0], (50, 50))
        self.assertEqual(p.bin_list()[1], (50, 60))
        self.assertTrue((0, 0, 0, 50, 20, None) in p.rect_list())
        self.assertTrue((1, 0, 0, 50, 40, None) in p.rect_list())
        self.assertTrue((1, 0, 40, 50, 20, None) in p.rect_list())
    
    def test_repack(self):
        """Test can be packed a second time"""
        p = packer.PackerBBF(pack_algo=guillotine.GuillotineBafSas,
                sort_algo=packer.SORT_NONE, rotation=False)
        p.add_bin(100, 100)
        p.add_rect(20, 20)
        p.pack()
        
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))

        # Add rectangles and repack
        p.add_rect(80, 80)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))
        self.assertEqual(p.rect_list()[1], (0, 20, 0, 80, 80, None))

    def test_repack_sorted(self):
        """Test can be packed a second time sorted"""
        p = packer.PackerBBF(pack_algo=guillotine.GuillotineBafSas,
                sort_algo=packer.SORT_LSIDE, rotation=False)
        p.add_bin(100, 100)
        p.add_rect(20, 20)
        p.pack()
        
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 20, None))

        # Add rectangles and repack
        p.add_rect(80, 80)
        p.pack()
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 80, 80, None))
        self.assertEqual(p.rect_list()[1], (0, 0, 80, 20, 20, None))



class TestPackerGlobal(TestCase):

    """
    GLOBAL: For each bin pack the rectangle with the best fitness.
    """
    def test_limit_cases(self):
        """Test pack works without rectangles and/or bins"""
        p = packer.PackerGlobal()
        p.add_bin(100, 100)
        p.add_bin(20, 20)
        p.pack()
        self.assertEqual(len(p.rect_list()), 0)
        self.assertEqual(len(p.bin_list()), 0)

        p = packer.PackerGlobal()
        p.add_rect(30, 30)
        p.add_rect(20, 20)
        p.pack()
        self.assertEqual(len(p.rect_list()), 0)
        self.assertEqual(len(p.bin_list()), 0)

        p = packer.PackerGlobal()
        p.pack()
        self.assertEqual(len(p.rect_list()), 0)
        self.assertEqual(len(p.bin_list()), 0)

    def test_best_selection(self):
        # Test rectangles with better fitness are placed first 
        p = packer.PackerGlobal(pack_algo=skyline.SkylineMwfl, 
                rotation=False)
        p.add_bin(100, 100)
        p.add_rect(40, 10)
        p.add_rect(100, 50)
        p.add_rect(90, 30)
        p.pack()

        self.assertEqual(len(p.rect_list()), 3)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 40, 10, None))
        self.assertEqual(p.rect_list()[1], (0, 0, 10, 90, 30, None))
        self.assertEqual(p.rect_list()[2], (0, 0, 40, 100, 50, None))
        
        # Test can handle more than one bin
        p = packer.PackerGlobal(pack_algo=skyline.SkylineMwfl, 
                rotation=False)
        p.add_bin(50, 50)
        p.add_bin(100, 100)
        p.add_rect(40, 40)
        p.add_rect(80, 80)
        p.add_rect(10, 10)
        p.pack()

        self.assertEqual(len(p.rect_list()), 3)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 10, 10, None))
        self.assertEqual(p.rect_list()[1], (0, 10, 0, 40, 40, None))
        self.assertEqual(p.rect_list()[2], (1, 0, 0, 80, 80, None))


    def test_fitness2(self):
        p = packer.PackerGlobal(pack_algo=guillotine.GuillotineBafSas, 
                rotation=False)

        p.add_bin(100, 100)
        p.add_rect(20, 10)
        p.add_rect(80, 10)
        p.add_rect(80, 80)
        p.pack()

        self.assertEqual(len(p.rect_list()), 3)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 80, 80, None))
        self.assertEqual(p.rect_list()[1], (0, 0, 80, 80, 10, None))
        self.assertEqual(p.rect_list()[2], (0, 0, 90, 20, 10, None))

    def test_repack(self):
        """Test can be packed a second time"""
        p = packer.PackerGlobal(pack_algo=guillotine.GuillotineBafSas, 
                rotation=False)
        p.add_bin(100, 100)
        p.add_rect(20, 10)
        p.pack()

        self.assertEqual(len(p.rect_list()), 1)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 20, 10, None))

        # Add more rectangles and repack
        p.add_rect(80, 10)
        p.add_rect(80, 80)
        p.pack()
        
        self.assertEqual(len(p.rect_list()), 3)
        self.assertEqual(p.rect_list()[0], (0, 0, 0, 80, 80, None))
        self.assertEqual(p.rect_list()[1], (0, 0, 80, 80, 10, None))
        self.assertEqual(p.rect_list()[2], (0, 0, 90, 20, 10, None))

class TestNewPacker(TestCase):

    def test_class(self):
        """Test newPacker returns correct Packer class"""
        # Test default options
        p = packer.newPacker()
        
        # Default mode Online BBF
        self.assertIsInstance(p, packer.PackerBBF)

        # Default rotations True
        self.assertEqual(p._rotation, True)

        # Default packing algorithm SkylineBlWm
        p.add_rect(100, 10)
        p.add_bin(10, 100)
        p.pack()
        self.assertIsInstance(p[0], skyline.SkylineBlWm)
        self.assertEqual(len(p[0]), 1)

        # Default sortin algorithm SORT_LSIDE
        self.assertEqual(p._sort_algo, packer.SORT_LSIDE)

    def test_rotation(self):
        """Test newPacker rotation argument"""
        p = packer.newPacker(rotation=False) 
        p.add_rect(100, 10)
        p.add_bin(10, 100)
        p.pack()
        self.assertEqual(len(p.rect_list()), 0)
        
        p = packer.newPacker(rotation=True) 
        p.add_rect(100, 10)
        p.add_bin(10, 100)
        p.pack()
        self.assertEqual(len(p.rect_list()), 1)

    def test_pack_algo(self):
        """Test NewPacker use correct PackingAlgorithm"""
        p = packer.newPacker(pack_algo=skyline.SkylineMwfl)
        p.add_rect(10, 10)
        p.add_bin(100, 100)
        p.pack()
        self.assertIsInstance(p[0], skyline.SkylineMwfl)

    def test_mode_offline(self):
        """Test newPacker returns correct Packer when in offline mode"""
        p = packer.newPacker(mode=packer.PackingMode.Offline, 
                bin_algo=packer.PackingBin.BNF)
        self.assertIsInstance(p, packer.PackerBNF)

        p = packer.newPacker(mode=packer.PackingMode.Offline,
                bin_algo=packer.PackingBin.BFF)
        self.assertIsInstance(p, packer.PackerBFF)
        
        p = packer.newPacker(mode=packer.PackingMode.Offline,
                bin_algo=packer.PackingBin.BBF)
        self.assertIsInstance(p, packer.PackerBBF)
        
        p = packer.newPacker(mode=packer.PackingMode.Offline,
                bin_algo=packer.PackingBin.Global)
        self.assertIsInstance(p, packer.PackerGlobal)

    def test_mode_online(self):
        """Test newPacker return correct Packer when in online mode"""
        p = packer.newPacker(mode=packer.PackingMode.Online,
                bin_algo=packer.PackingBin.BNF)
        self.assertIsInstance(p, packer.PackerOnlineBNF)

        p = packer.newPacker(mode=packer.PackingMode.Online,
                bin_algo=packer.PackingBin.BFF)
        self.assertIsInstance(p, packer.PackerOnlineBFF)

        p = packer.newPacker(mode=packer.PackingMode.Online,
                bin_algo=packer.PackingBin.BBF)
        self.assertIsInstance(p, packer.PackerOnlineBBF)

        with self.assertRaises(AttributeError):
            p = packer.newPacker(mode=packer.PackingMode.Online,
                    bin_algo=packer.PackingBin.Global)

    def test_offline_sorting(self):
        """Test newPacker uses provided sort algorithm"""
        p = packer.newPacker(mode=packer.PackingMode.Offline,
                bin_algo=packer.PackingBin.BFF, 
                sort_algo=packer.SORT_RATIO)
        self.assertEqual(p._sort_algo, packer.SORT_RATIO)
        
        # Test sort_algo is ignored when not applicable
        p = packer.newPacker(mode=packer.PackingMode.Offline,
                bin_algo=packer.PackingBin.Global, 
                sort_algo=packer.SORT_RATIO)

        p = packer.newPacker(mode=packer.PackingMode.Online,
                bin_algo=packer.PackingBin.BFF, 
                sort_algo=packer.SORT_RATIO)