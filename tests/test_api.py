# -*- coding: utf-8 -*-
from io import BytesIO
from unittest import TestCase

from datasets.api import app, parse_args


class TestApi(TestCase):
    maxDiff = None

    def gif_file(self):
        return (BytesIO(
            b'GIF89a=\x00D\x00\xf7\xa8\x00\x9a,3\xff\xc0\xc0\xef\xc0\xc0uXg\xfc\xf9\xf7\x993\x00\xff\xec\xec\xff\xa0\xa0\xe5\xcc\xbf\xcf\x9f\x87\x0f\xef\xef\x7f\x7f\x7f\xef\x0f\x0f\xdf\x1f\x1f\xff&&_\x9f\x9f\xffYY\xbf??5\xa5\xc2\xff\xff\xff\xac\x16\x19\xb2&\x00\xf8\x13\x10\xc2& \xdf`PP\x84\x9b\xf8\x03\x00\xb5\x0b\x0c\xdf\x0f\x00>\x9a\xb5\x87BM\x7f`P\xd2\xa5\x8f\xcc\x19\x00\xa5,\x00\xec\xd9\xcf\xe5\x0c\x00\xeb\t\x00\xff\xd9\xd9\xc7\x0c\x0c\x0f\x0f\x0f\xffyy~MZ\xfb\t\x08\xe5M@\xfb__\xff33\xcf\x90x\xf2\xe5\xdf\xc3\x06\x06\xbf\t\x08\xff\xb3\xb3\xd9\xb2\x9f\xff\x06\x06\xac)\x00\xff\xc6\xc6\x0c\t\x08\xf9\xf2\xef\xc9s`\xb8#\x00\x9f/\x00\xff__\xff\x8c\x8c\xc5\x1c\x00\xdf33\xffpp\xcf\x19\x19\xc0\x13\x10\xbf\x90x\xf7YY\xff\xf6\xf6\xe7??\xd7&&\xefLL2& \xdf\xbf\xaf\xbf\xbf\xbf???\xc5M@cn\x81_\x00\x00___\xcb00\xd8\x13\x00YC8\x80\x80\x80\xf3RRsVH\xc490\x10\x10\x10\x917@\xf2\x06\x00\xcf@@\xca\x86pooo\xa3!&\xc1\x1d\x18\xcf//\x1f\x1f\x1f\xdf\x00\x00\xd2\x16\x00\xcb\x90x\xbf\x1f\x00\x19\x13\x10\xf3\xd0\xd0\xe399&\x1d\x18Yy\x8e\x8f\x8f\x8f\xff\xa9\xa9\xcb\x13\x13\xbf00SF@\xb6& >\x1d\x18\xfb\xdd\xdd@@@\x99\x93\x90\xff\xbc\xbc\x7fPP\xaf\xaf\xaf\xc6VHzsp\x93& \xb7pp\xb3\x86ptPP|pp\xafOO\xd0\xd0\xd0\xef\xef\xefL90\xbc\xa9\xa0o0(\xeb\xb0\xb0\xff\xe0\xe0\xff\xd0\xd0\x870(K0(\xc9|h\x9f__lct\xebFF\xcf\xcf\xcf\xe0\xe0\xe0b& \xff  },(@0(\xa9\x93\x88\xa6|h\x1f\xdf\xdf\xd5\xac\x97\xe2\xc5\xb7\xc7`POOO\x9cyhppp\xff\x80\x80\xff\x96\x96\xd7``\xcc\x99\x7f,\xb0\xcf\xbf\x00\x00\x00\x00\x00\x00\xff\xff\xff\x00\x00\xffff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\xa8\x00,\x00\x00\x00\x00=\x00D\x00\x00\x08\xff\x00Q\t\x1cH\xb0\xa0\xc1\x83\x08\x13*\\\xc8\xb0\xa1\xc0\x1b\x07\x0c8\x9cHq\xa1\x89\x14\xa72F\xac\xc8\xb1\xa2\t\x1f\x19Cj\x94\xd8\xb1$B\x03\x07D\xaa\x1ci\xb2%*#3V\xcad\xe9\xb2\xa2\x9d 3s\x9e\xdaX\x93!"\x8c:\x83\xf2\xeci\xf0c\xd0\xa3!\x87\x12E\x89\xb4iR\x92.a:\x9d\xfa\xb4\xe5\x0c\x9cT\xb3\xee\x84:\xf1\x06P\xad`\x95*4\n\xb6l\xd5\x84\x06>\x99]\x1b\xb2\xc5\x9c\x83F\xda\xb0\x9d{\xe4\x84\x00\x83W\xe7\xaeM\xe2f\xd4\xa8\xbb\x03\xbd\xea5kE\x88_\xbf\x80\x0fy\x1a\\\xb6\x08\x92\xc3\x87\x01\x070\xe5\x00\x02\xe3\xa9-\x80\xc4\x80\x1cY\xe0dS\x94-_\x0ezd3\xe7\xce\xa8>\x83\x0e=Zf\x92\x13\xa7Gm\x18 \xe1\xaf\xe7\xd5\xb8+\xb7\xceX8\xf6(\xda\xa2D\xd9N\x8d\xbb\xb8n\xc6\x8e}\x8f\xfa\x12<\xf8\xf0\xcf\x11\x1a\x14\x07}|mf\xdf\x00\x9elP\xd1\\\xb8dSaJ\x95\xffz }zu\xadiLs\xa6\xb0&8\x80\x01\xdd\x9f\x9b\x8a ^<\xf9\xe9\xac\xa9:\x82\x1d{\x83\x84\xe6\xef\xc5\xf7\x1d}\xf5\xd9W\x9eq\xa2\x1d\x95\x84a\xb1\xa9\xb0\x01\x00\xdd\x05\xd8\x9c|\x04\x16X\x8a\x02\x0b0\x80\x9f\x0b=\xe8\x94\\l\x1et \n\x00\x10\x02\x08\xdf\x84\x03ZX \x86\x1a\x16W\x03\x87+]\xe7[\x06\x00\x96\xe8\xde\x89\xce\xa5\xa8\xe2\x8a\x19N\xf7b\x87\x19\xa5\x17\x1b\x05\xa3P\x10\xa1\x8d#\xe2X\x9b\x8e;\xf2\xd8"n/\xd6\xd5\xdf\x13\xa2x\x80$\x89\x11\x9e\xd8\x81\x16\x146\xb9#\x8b\xd3\xf9\xe6\xc1\x7f\xa2\x0cp\xe5\x99\x12\xa8\x80\xdad\x15zi!\x98\xab\xf9Ff\x99gvG$g\xdf1\xa0\x80\x9bM\xc2\t\x19\x00\x19p\xd9\x9d\x99G6\xd7Hl\xdf\x99\xc2\xc8\x9e|~\t\x88)~Q@c\x99\xa3\x0cZg\x06\x00\xf8\x96\xa8)\x0c,\xc0h\xa3\x05^\x02\xe9(\x93Rji\x84\xcb)\'\x1fn\x9d~\nj)\xa3\x0e\xffZis\x84\x06\xd7\x81\xaak\xae\xc6\x01\x07\xa0\xb5\xfa*\xac~\xc9z\xaa\x04\x03l\x80+b\xb7\x81V@\x01$\xac\xd6\xe9\xab\xb1\xd2:kpj\x0ep\xe7\xb1\xab\x9aRA\x01!\x14\xd7\xc0\x03\x8dF\x1b\xdc\x00\xd3\x8ar-\xb6\xc8\x12\x07Z\t\x15\xf0:\xdd\xb7n\x8ak\xaa(\x1ddz\xac\x14\x86\x80\x92+~\xf8\xc1\xbb\xa3\xbc\xe4\xae\xe1\x01\xbaR\xfcAG\'\\\xa4\xab\x1a\xbf\xef\x82k\xa1\xbc\x03\xa3\xeb\xd7\x1d\xa4T\xcc\x87\xc2\xc5qP\x02\xc3\xab\xf9+\x9e\xb8OH\xec\xd7\x1bYTL\x8a\x1f~\xa1\x91\xecj"\xd8\xc01n\xfe\x8e\xdaA\x06\xe7\xa2;\t)Q\xb0AJ\x15\\\xa8\xbc2h!\x14\xe0\xee\xcb\xa05\x10\xc6\xa8"s&\x07\n\x13L\xb0sA\x0b\x9b\xa2\x81\x08"h\xf02\x0f\x15\xe0\x964g2\xa8\xd1D\xd3\xa4\xe8\x01\xf5t\x1c\x14`\xc6\xcb\xcbN\x11\xe7\xd6\x87]@\xca\xd7\x8f\x90\xf2\x01\x08#\x10t\x80$\xc5\x99\xc1-\xc7?\x14\xff@\xc6\xdal\x8f\xe2\x04)b0\xb1\t)}\x84\x12J&\x04\x05\x02\xc5\x18\xb8\xd9P\xc0\x0f\x1c\x93`5h\x81_\xb0H(j\x98\xacD( \xc0`P\xc5\x8f\x83\xa6\xc1\xb6;l1\x9d\x06\x1bk\x9d4\x18:(\x1e\n\x15&sR\xb7A9\xc0Q\xf1 \x18X\x00Z\xdf<\x84\xa0:h$H^\x1cgC\\\xa0\xdc\x10\x9a\xc8\xae8\x11gdQ\x07\x01\x07!\x10\n\x11W| {\xef\xa6\x90\xb0m\x01"T B\x01<\xa8\xed\xba_X|pE\x1e\xa7\xc9\xe0D\x19\xce\xcb\xbe\x04\xf5\x08\x11\x80@\x02\xf1+\xce}\t!\xecP\xc1\x0ed\xb8\xdc\xf9\x86\xa0\x88\x8aQA\x06\x90\xc1\x02\xfc\xf2G\x83\x1c4\xc4~\xf8\xcb\x1f\xf7^v\x98D\x98\x0c\x07\xca\x1b\xc5\x05\xba\x90\xbfP`Bt\x14\x81`\x07\'\xc8/\xbf\xc8@\toC\x01)\x9c\x00\xbb\x0e\xd2\xcd$"\x94\xa0\xef\xf0\xe3\x978\xe0l\x02^ \x05\x07\xf3\x97\x00\x04\xd0\xaf%1t\xde\x0b|X\xb0\x820\x8db\x0f\xa4`\xc2\x04\x16@\x8a\x0e\xce\x8f(\x02\t\xa2\xec\x86X\xc4\xb5\x15"\x898\xc4A\xfc\x1a\x08\xc5\x82HQqT\xc4\xdc("A\n<\x08\x02\x05\x94\x90\x1d\r@\xd8E\x83|1\x14T\xbc\x80\x0e>@\n\x14\x88An\xa0\xbb]\x1b\x13\xf2F\xd9Y\xc2dg\xe8\xe1\x1e\x1d\xd2\xc7P\xa0\x10\x07\x84\xf8\xe1 \x1fx\xbf\xfc\x11\xa1\x12\x90XdG\x82\xb8FI\x02q\t/\xb4\xa4&[\x12\x10\x00;'
        ), "image.gif",)

    def iris_file(self):
        return (BytesIO((
            f"\"01/01/2000\",5.1,3.5,1.4,0.2,\"Iris-setosa\"\n"
            f"\"01/01/2001\",4.9,3.0,1.4,0.2,\"Iris-setosa\"\n"
            f"\"01/01/2002\",4.7,3.2,1.3,0.2,\"Iris-setosa\"\n"
            f"\"01/01/2003\",4.6,3.1,1.5,0.2,\"Iris-setosa\"\n"
        ).encode()), "iris.data",)

    def iris_featuretypes(self):
        return (BytesIO((
            f"DateTime\n"
            f"Numerical\n"
            f"Numerical\n"
            f"Numerical\n"
            f"Numerical\n"
            f"Categorical\n"
        ).encode()), "featuretypes.txt",)

    def boston_file(self):
        return (BytesIO((
            f"0.00632;18;2.31;0;0.538;6.575;65.2;4.09;1;296;15.3;396.9;4.98;24\n"
            f"0.02731;0;7.07;0;0.469;6.421;78.9;4.9671;2;242;17.8;396.9;9.14;21.6\n"
            f"0.02729;0;7.07;0;0.469;7.185;61.1;4.9671;2;242;17.8;392.83;4.03;34.7\n"
            f"0.03237;0;2.18;0;0.458;6.998;45.8;6.0622;3;222;18.7;394.63;2.94;33.4\n"
            f"0.06905;0;2.18;0;0.458;7.147;54.2;6.0622;3;222;18.7;396.9;5.33;36.2\n"
        ).encode("utf-8-sig")), "boston.data",)

    def titanic_file(self):
        return (BytesIO((
            f"PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked\n"
            f"11	1	3	Sandström, Miss. Marguerite Rut	female	4	1	1	PP 9549	16.7	G6	S\n"
            f"15	0	3	Veström, Miss. Hulda Amanda Adolfina	female	14	0	0	350406	7.8542		S\n"
            f"29	1	3	O‘Dwyer, Miss. Ellen “Nellie”	female		0	0	330959	7.8792		Q\n"
            f"44	1	2	Laroche, Miss. Simonne Marie Anne Andrée	female	3	1	2	SC/Paris 2123	41.5792		C\n"
            f"84	0	1	Carraú, Mr. Francisco M	male	28	0	0	113059	47.1		S\n"
            f"92	0	3	Andreasson, Mr. Pål Edvin	male	20	0	0	347466	7.8542		S\n"
            f"130	0	3	Ekström, Mr. Johan	male	45	0	0	347061	6.975		S\n"
            f"134	1	2	Weisz, Mrs. Leopold – Mathilde Francoise Pede	female	29	1	0	228414	26		S\n"
        ).encode("windows-1252")), "titanic.csv",)

    def test_parse_args(self):
        parser = parse_args([])
        self.assertEqual(parser.port, 8080)
        self.assertFalse(parser.enable_cors)
        parser = parse_args(["--enable-cors", "--port", "3000"])
        self.assertEqual(parser.port, 3000)
        self.assertTrue(parser.enable_cors)

    def test_ping(self):
        with app.test_client() as c:
            rv = c.get("/")
            result = rv.get_data(as_text=True)
            expected = "pong"
            self.assertEqual(result, expected)

    def test_list_datasets(self):
        with app.test_client() as c:
            rv = c.get("/datasets")
            result = rv.get_json()
            self.assertIsInstance(result, list)

    def test_create_dataset(self):
        with app.test_client() as c:
            rv = c.post("/datasets", data={})
            result = rv.get_json()
            expected = {"message": "No file part"}
            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 400)
            rv = c.post("/datasets", data={"file": (BytesIO(), "")})
            result = rv.get_json()
            expected = {"message": "No selected file"}            
            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 400)

            rv = c.post("/datasets", data={
                "file": self.iris_file(),
                "featuretypes": (BytesIO(b"date\n" +
                                         b"float\n" +
                                         b"float\n" +
                                         b"float\n" +
                                         b"float\n" +
                                         b"string"), "featuretypes.txt"),
            })
            result = rv.get_json()
            expected = {
                "message": "featuretype must be one of DateTime, Numerical, Categorical"}

            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 400)

            rv = c.post("/datasets", data={
                "file": self.iris_file(),
                "featuretypes": (BytesIO(b"DateTime"), "featuretypes.txt"),
            })
            result = rv.get_json()
            expected = {
                "message": "featuretypes must be the same length as the DataFrame columns"}
                

            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 400)

            rv = c.post("/datasets", data={
                "file": self.iris_file(),
            })
            result = rv.get_json()
            expected = {
                "columns": [
                    {"name": "col0", "featuretype": "DateTime"},
                    {"name": "col1", "featuretype": "Numerical"},
                    {"name": "col2", "featuretype": "Numerical"},
                    {"name": "col3", "featuretype": "Numerical"},
                    {"name": "col4", "featuretype": "Numerical"},
                    {"name": "col5", "featuretype": "Categorical"},
                ],
                "filename": "iris.data",
            }
            # name is machine-generated
            # we assert it exists, but we don't assert their values
            self.assertIn("name", result)
            del result["name"]
            
            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 200)

            rv = c.post("/datasets", data={
                "file": self.boston_file(),
            })
            result = rv.get_json()
            expected = {
                "columns": [
                    {"name": "col0", "featuretype": "Numerical"},
                    {"name": "col1", "featuretype": "Numerical"},
                    {"name": "col2", "featuretype": "Numerical"},
                    {"name": "col3", "featuretype": "Numerical"},
                    {"name": "col4", "featuretype": "Numerical"},
                    {"name": "col5", "featuretype": "Numerical"},
                    {"name": "col6", "featuretype": "Numerical"},
                    {"name": "col7", "featuretype": "Numerical"},
                    {"name": "col8", "featuretype": "Numerical"},
                    {"name": "col9", "featuretype": "Numerical"},
                    {"name": "col10", "featuretype": "Numerical"},
                    {"name": "col11", "featuretype": "Numerical"},
                    {"name": "col12", "featuretype": "Numerical"},
                    {"name": "col13", "featuretype": "Numerical"},
                ],
                "filename": "boston.data",
            }
            # name is machine-generated
            # we assert it exists, but we don't assert their values
            self.assertIn("name", result)
            del result["name"]

            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 200)

            rv = c.post("/datasets", data={
                "file": self.titanic_file(),
            })
            result = rv.get_json()
            expected = {
                "columns": [
                    {"name": "PassengerId", "featuretype": "Numerical"},
                    {"name": "Survived", "featuretype": "Numerical"},
                    {"name": "Pclass", "featuretype": "Numerical"},
                    {"name": "Name", "featuretype": "Categorical"},
                    {"name": "Sex", "featuretype": "Categorical"},
                    {"name": "Age", "featuretype": "Numerical"},
                    {"name": "SibSp", "featuretype": "Numerical"},
                    {"name": "Parch", "featuretype": "Numerical"},
                    {"name": "Ticket", "featuretype": "Categorical"},
                    {"name": "Fare", "featuretype": "Numerical"},
                    {"name": "Cabin", "featuretype": "Categorical"},
                    {"name": "Embarked", "featuretype": "Categorical"},
                ],
                "filename": "titanic.csv",
            }
            # name is machine-generated
            # we assert it exists, but we don't assert their values
            self.assertIn("name", result)
            del result["name"]
            
            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 200)

            rv = c.post("/datasets", data={
                "file": self.iris_file(),
                "featuretypes": self.iris_featuretypes(),
            })
            result = rv.get_json()
            expected = {
                "columns": [
                    {"name": "col0", "featuretype": "DateTime"},
                    {"name": "col1", "featuretype": "Numerical"},
                    {"name": "col2", "featuretype": "Numerical"},
                    {"name": "col3", "featuretype": "Numerical"},
                    {"name": "col4", "featuretype": "Numerical"},
                    {"name": "col5", "featuretype": "Categorical"},
                ],
                "filename": "iris.data",
            }
            self.assertIn("name", result)
            del result["name"]
            
            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 200)

            rv = c.post("/datasets", data={
                "file": self.gif_file(),
            })
            result = rv.get_json()
            expected = {
                "filename": "image.gif",
            }
            self.assertIn("name", result)
            del result["name"]

            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 200)

    def test_get_dataset(self):
        with app.test_client() as c:
            rv = c.get("/datasets/UNK")
            result = rv.get_json()
            expected = {"message": "The specified dataset does not exist"}
            
            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 404)

            rv = c.post("/datasets", data={
                "file": self.iris_file(),
            })
            name = rv.get_json().get("name")

            rv = c.get(f"/datasets/{name}")
            result = rv.get_json()
            expected = {
                "columns": [
                    {"name": "col0", "featuretype": "DateTime"},
                    {"name": "col1", "featuretype": "Numerical"},
                    {"name": "col2", "featuretype": "Numerical"},
                    {"name": "col3", "featuretype": "Numerical"},
                    {"name": "col4", "featuretype": "Numerical"},
                    {"name": "col5", "featuretype": "Categorical"},
                ],
                "filename": "iris.data",
            }
            # name is machine-generated
            # we assert it exists, but we don't check its value
            self.assertIn("name", result)
            del result["name"]

            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 200)

    def test_list_columns(self):
        with app.test_client() as c:
            rv = c.get("/datasets/UNK/columns")

            result = rv.get_json()
            expected = {"message": "The specified dataset does not exist"}
            
            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 404)

            rv = c.post("/datasets", data={
                "file": self.iris_file(),
            })
            name = rv.get_json().get("name")

            rv = c.get(f"/datasets/{name}/columns")
            result = rv.get_json()
            expected = [
                {"name": "col0", "featuretype": "DateTime"},
                {"name": "col1", "featuretype": "Numerical"},
                {"name": "col2", "featuretype": "Numerical"},
                {"name": "col3", "featuretype": "Numerical"},
                {"name": "col4", "featuretype": "Numerical"},
                {"name": "col5", "featuretype": "Categorical"},
            ]

            self.assertListEqual(expected, result)
            self.assertEqual(rv.status_code, 200)

    def test_update_column(self):
        with app.test_client() as c:
            rv = c.patch("/datasets/UNK/columns/col0", json={
                "featuretype": "Numerical"
            })
            result = rv.get_json()
            expected = {"message": "The specified dataset does not exist"}
            
            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 404)

            rv = c.post("/datasets", data={
                "file": self.iris_file(),
            })
            name = rv.get_json().get("name")

            rv = c.patch(f"/datasets/{name}/columns/unk", json={
                "featuretype": "Numerical"
            })
            result = rv.get_json()
            expected = {"message": "The specified column does not exist"}

            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 404)

            rv = c.patch(f"/datasets/{name}/columns/col0", json={
                "featuretype": "Invalid"
            })
            result = rv.get_json()
            expected = {
                "message": "featuretype must be one of DateTime, Numerical, Categorical"}

            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 400)

            rv = c.patch(f"/datasets/{name}/columns/col0", json={
                "featuretype": "Numerical"
            })
            result = rv.get_json()
            expected = {
                "name": "col0",
                "featuretype": "Numerical"
            }

            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 200)

            rv = c.post("/datasets", data={
                "file": self.gif_file(),
            })
            name = rv.get_json().get("name")

            rv = c.patch(f"/datasets/{name}/columns/unk", json={
                "featuretype": "Numerical"
            })

            result = rv.get_json()
            expected = {"message": "The specified column does not exist"}

            self.assertDictEqual(expected, result)
            self.assertEqual(rv.status_code, 404)
