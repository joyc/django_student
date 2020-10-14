from django.test import TestCase, Client

from .models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='赵钱',
            sex=1,
            email='ts@demo.com',
            profession='工人',
            qq='67575587',
            phone='123342321142',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='刘无能',
            sex=1,
            email='lwuneng@code.com',
            profession='程序员',
            qq='47571587',
            phone='13933232112',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容不一致！')

    def test_filter(self):
        Student.objects.create(
            name='刘无能',
            sex=1,
            email='lwuneng@code.com',
            profession='程序员',
            qq='47571587',
            phone='13933232112',
        )
        name = '赵钱'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名为{}的记录。'.format(name))

    def test_get_index(self):
        """测试首页的可用性"""
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='23@df.com',
            profession='程序员',
            qq='234234',
            phone='32425343',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content,
                        'response content must contain `test_for_post`')
