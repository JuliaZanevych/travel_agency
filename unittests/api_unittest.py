import unittest
import uuid

from flask_testing import TestCase

from app import app

AUTHORIZATION_HEADER = 'Authorization'

INVALID_AUTHORIZATION_HEADER = 'SnVsaWE2NDpKdTY0bGlh'
NON_BASIC_AUTHORIZATION_HEADER = 'Bearer SnVsaWE2NDpKdTY0bGlh'
INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER = 'Basic SnVsaWE2NDpKdTY0bGl'
INVALID_PAYLOAD_AUTHORIZATION_HEADER = 'Basic SnVsaWE0NzlKdTIzNGxpYTk='
NON_ADMIN_AUTHORIZATION_HEADER = 'Basic SnVsaWE2NDpKdTY0bGlh'
ADMIN_AUTHORIZATION_HEADER = 'Basic SnVsaWE0NzpKdTIzNGxpYQ=='

CUSTOMER_API = '/customers'
COUNTRY_API = '/countries'
TOUR_API = '/tours'
TOURISR_ATTRACTION_API = '/tourist-attractions'
CITY_API = '/cities'
TRANSPORTATION_API = '/transportations'
CUSTOMER_ADDRESS_API = '/customer_addresses'
HOTEL_API = '/hotels'
VOUCHER_API = '/vouchers'
ROLE_API = '/roles'
PERMISSION_API = '/permissions'


class BaseTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app


class Test(BaseTestCase):
    '''
    Unit tests for Hello World test API
    '''
    def test_hello_world(self):
        self.assert_200(self.client.get('/api/v1/hello-world-47'))

    '''
    Unit tests for Customers
    '''

    def test_post_customer__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_API}/post'))

    def test_post_customer__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_customer__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_customer__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_customer__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_customer__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{CUSTOMER_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_customer__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/1/get'))

    def test_get_customer__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_customer__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_customer__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_customer__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_customer_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/get'))

    def test_get_customer_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_customer_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_customer_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_customer_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_customer_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{CUSTOMER_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_customer_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{CUSTOMER_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_customer__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_API}/1/update'))

    def test_update_customer__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_customer__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_customer__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_customer__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_customer__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{CUSTOMER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_customer__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_API}/1/delete'))

    def test_delete_customer__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_customer__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_customer__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_customer__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_customer__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{CUSTOMER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_customer(self):
        customer_creating_payload = {
            "username": uuid.uuid4().hex,
            "first_name": "Julia",
            "middle_name": "Bogdanivna",
            "last_name": "Zanevych",
            "phone": "0731213007",
            "date_of_birthday": "2002-07-14",
            "gender": "FEMALE",
            "is_covid_vaccinated": True,
            "is_blocked": True,
            "password_hash": uuid.uuid4().hex,
            "role_id": 1
        }

        create_response = self.client.post(f'{CUSTOMER_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=customer_creating_payload)

        self.assertStatus(create_response, 201)

        created_customer = create_response.json
        customer_id = created_customer['id']

        get_response = self.client.get(f'{CUSTOMER_API}/{customer_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)

        customer_updating_payload = {
            "username": uuid.uuid4().hex,
            "first_name": "Julia",
            "middle_name": "Bogdanivna",
            "last_name": "Zanevych",
            "phone": "0731213007",
            "date_of_birthday": "2002-07-14",
            "gender": "FEMALE",
            "is_covid_vaccinated": True,
            "is_blocked": True,
            "password_hash": uuid.uuid4().hex,
            "role_id": 1
        }

        self.assert_200(self.client.put(f'{CUSTOMER_API}/{customer_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=customer_updating_payload))

        get_response_after_update = self.client.get(f'{CUSTOMER_API}/{customer_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)

        self.assertStatus(self.client.delete(f'{CUSTOMER_API}/{customer_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{CUSTOMER_API}/{customer_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{CUSTOMER_API}/{customer_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=customer_updating_payload))
        self.assert_404(self.client.delete(f'{CUSTOMER_API}/{customer_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_post_customer__when_duplicated_username__expect_409(self):
        self.assert_status(self.client.post(f'{CUSTOMER_API}/post',
                                            headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                            json={
                                                "username": 'Julia64',
                                                "first_name": "Julia",
                                                "middle_name": "Bogdanivna",
                                                "last_name": "Zanevych",
                                                "phone": "0731213007",
                                                "date_of_birthday": "2002-07-14",
                                                "gender": "FEMALE",
                                                "is_covid_vaccinated": True,
                                                "is_blocked": True,
                                                "password_hash": uuid.uuid4().hex,
                                                "role_id": 1
                                            }),
                           409)

    '''
    Unit tests for Countries
    '''

    def test_post_country__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{COUNTRY_API}/post'))

    def test_post_country__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{COUNTRY_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_country__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{COUNTRY_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_country__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{COUNTRY_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_country__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{COUNTRY_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_country__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{COUNTRY_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_country__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/1/get'))

    def test_get_country__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_country__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_country__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_country__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_country_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/get'))

    def test_get_country_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_country_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_country_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_country_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{COUNTRY_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_country_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{COUNTRY_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_country_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{COUNTRY_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_country__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{COUNTRY_API}/1/update'))

    def test_update_country__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{COUNTRY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_country__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{COUNTRY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_country__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{COUNTRY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_country__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{COUNTRY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_country__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{COUNTRY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_country__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{COUNTRY_API}/1/delete'))

    def test_delete_country__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{COUNTRY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_country__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{COUNTRY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_country__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{COUNTRY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_country__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{COUNTRY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_country__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{COUNTRY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_country(self):
        country_creating_payload = {
            "country_name": uuid.uuid4().hex,
            "official_language": "Ukrainian",
            "population": 45000000,
            "details": "details"
        }

        create_response = self.client.post(f'{COUNTRY_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=country_creating_payload)

        self.assertStatus(create_response, 201)

        created_country = create_response.json
        country_id = created_country['id']

        get_response = self.client.get(f'{COUNTRY_API}/{country_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)
        assert get_response.json == created_country
        assert get_response.json == {**{'id': country_id}, **country_creating_payload}

        country_updating_payload = {
            "country_name": uuid.uuid4().hex,
            "official_language": "Ukrainian",
            "population": 450444444,
            "details": "details"
        }

        self.assert_200(self.client.put(f'{COUNTRY_API}/{country_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=country_updating_payload))

        get_response_after_update = self.client.get(f'{COUNTRY_API}/{country_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)
        assert get_response_after_update.json == {**{'id': country_id}, **country_updating_payload}

        self.assertStatus(self.client.delete(f'{COUNTRY_API}/{country_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{COUNTRY_API}/{country_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{COUNTRY_API}/{country_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=country_updating_payload))
        self.assert_404(self.client.delete(f'{COUNTRY_API}/{country_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_post_country__when_duplicated_country_name__expect_409(self):
        self.assert_status(self.client.post(f'{COUNTRY_API}/post',
                                            headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                            json={
                                                "country_name": "Ukraine",
                                                "official_language": "Ukrainian",
                                                "population": 45000000,
                                                "details": "details"
                                            }),
                           409)

    '''
    Unit tests for Tours
    '''

    def test_post_tour__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOUR_API}/post'))

    def test_post_tour__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOUR_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_tour__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOUR_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_tour__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOUR_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_tour__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOUR_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_tour__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{TOUR_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_tour__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/1/get'))

    def test_get_tour__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_tour__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_tour__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_tour__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_tour_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/get'))

    def test_get_tour_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_tour_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_tour_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_tour_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOUR_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_tour_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{TOUR_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_tour_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{TOUR_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_tour__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOUR_API}/1/update'))

    def test_update_tour__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOUR_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_tour__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOUR_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_tour__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOUR_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_tour__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOUR_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_tour__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{TOUR_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_tour__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOUR_API}/1/delete'))

    def test_delete_tour__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOUR_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_tour__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOUR_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_tour__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOUR_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_tour__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOUR_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_tour__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{TOUR_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_tour(self):
        tour_creating_payload = {
            "name": uuid.uuid4().hex,
            "price": 300,
            "person_count": 3,
            "start_time": "2021-09-19",
            "end_time": "2021-09-25",
            "description": "Cool tour on Egypt",
            "recommended_pocket_money": 150,
            "tourist_attraction_ids": [
                1,
                2,
                3,
                4
            ]
        }

        create_response = self.client.post(f'{TOUR_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=tour_creating_payload)

        self.assertStatus(create_response, 201)

        created_tour = create_response.json
        tour_id = created_tour['id']

        get_response = self.client.get(f'{TOUR_API}/{tour_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)
        assert get_response.json == created_tour

        tour_updating_payload = {
            "name": uuid.uuid4().hex,
            "price": 590,
            "person_count": 2,
            "start_time": "2021-09-19",
            "end_time": "2021-09-25",
            "description": "Cool tour on Egypt",
            "recommended_pocket_money": 200,
            "tourist_attraction_ids": [
                3,
                4,
                5,
                6
            ]
        }

        self.assert_200(self.client.put(f'{TOUR_API}/{tour_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=tour_updating_payload))

        get_response_after_update = self.client.get(f'{TOUR_API}/{tour_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)

        self.assertStatus(self.client.delete(f'{TOUR_API}/{tour_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{TOUR_API}/{tour_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{TOUR_API}/{tour_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=tour_updating_payload))
        self.assert_404(self.client.delete(f'{TOUR_API}/{tour_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_post_tour__when_duplicated_name__expect_409(self):
        self.assert_status(self.client.post(f'{TOUR_API}/post',
                                            headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                            json={
                                                "name": "Travelmania",
                                                "price": "300",
                                                "person_count": "3",
                                                "start_time": "2021-09-19",
                                                "end_time": "2021-09-25",
                                                "description": "Cool tour on Egypt",
                                                "recommended_pocket_money": 150,
                                                "tourist_attraction_ids": [
                                                    1,
                                                    2,
                                                    3
                                                ]
                                            }),
                           409)

    '''
    Unit tests for Tourist_attraction
    '''

    def test_post_tourist_attraction__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOURISR_ATTRACTION_API}/post'))

    def test_post_tourist_attraction__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOURISR_ATTRACTION_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_tourist_attraction__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOURISR_ATTRACTION_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_tourist_attraction__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOURISR_ATTRACTION_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_tourist_attraction__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TOURISR_ATTRACTION_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_tourist_attraction__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{TOURISR_ATTRACTION_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/1/get'))

    def test_get_tourist_attraction__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/get'))

    def test_get_tourist_attraction_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TOURISR_ATTRACTION_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{TOURISR_ATTRACTION_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_tourist_attraction_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{TOURISR_ATTRACTION_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_tourist_attraction__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOURISR_ATTRACTION_API}/1/update'))

    def test_update_tourist_attraction__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOURISR_ATTRACTION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_tourist_attraction__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOURISR_ATTRACTION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_tourist_attraction__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOURISR_ATTRACTION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_tourist_attraction__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TOURISR_ATTRACTION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_tourist_attraction__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{TOURISR_ATTRACTION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_tourist_attraction__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOURISR_ATTRACTION_API}/1/delete'))

    def test_delete_tourist_attraction__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOURISR_ATTRACTION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_tourist_attraction__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOURISR_ATTRACTION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_tourist_attraction__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOURISR_ATTRACTION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_tourist_attraction__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TOURISR_ATTRACTION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_tourist_attraction__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{TOURISR_ATTRACTION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_tourist_attraction(self):
        tourist_attraction_creating_payload = {
            "name": "Sharm",
            "type": "EXCURSION",
            "city_id": 1,
            "details": "Curious tour of the underground city"
        }

        create_response = self.client.post(f'{TOURISR_ATTRACTION_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=tourist_attraction_creating_payload)

        self.assertStatus(create_response, 201)

        created_tourist_attraction = create_response.json
        tourist_attraction_id = created_tourist_attraction['id']

        get_response = self.client.get(f'{TOURISR_ATTRACTION_API}/{tourist_attraction_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)
        assert get_response.json == created_tourist_attraction
        assert get_response.json == {**{'id': tourist_attraction_id}, **tourist_attraction_creating_payload}

        tourist_attraction_updating_payload = {
            "name": "Sharm34",
            "type": "EXCURSION",
            "city_id": 2,
            "details": "Curious tour of the underground city"
        }

        self.assert_200(self.client.put(f'{TOURISR_ATTRACTION_API}/{tourist_attraction_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=tourist_attraction_updating_payload))

        get_response_after_update = self.client.get(f'{TOURISR_ATTRACTION_API}/{tourist_attraction_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)
        assert get_response_after_update.json == {**{'id': tourist_attraction_id},
                                                  **tourist_attraction_updating_payload}

        self.assertStatus(self.client.delete(f'{TOURISR_ATTRACTION_API}/{tourist_attraction_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{TOURISR_ATTRACTION_API}/{tourist_attraction_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{TOURISR_ATTRACTION_API}/{tourist_attraction_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=tourist_attraction_updating_payload))
        self.assert_404(self.client.delete(f'{TOURISR_ATTRACTION_API}/{tourist_attraction_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    '''
    Unit tests for Cities
    '''

    def test_post_city__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CITY_API}/post'))

    def test_post_city__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CITY_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_city__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CITY_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_city__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CITY_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_city__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CITY_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_city__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{CITY_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_city__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/1/get'))

    def test_get_city__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_city__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_city__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_city__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_city_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/get'))

    def test_get_city_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_city_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_city_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_city_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CITY_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_city_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{CITY_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_city_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{CITY_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_city__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CITY_API}/1/update'))

    def test_update_city__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CITY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_city__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CITY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_city__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CITY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_city__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CITY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_city__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{CITY_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_city__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CITY_API}/1/delete'))

    def test_delete_city__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CITY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_city__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CITY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_city__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CITY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_city__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CITY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_city__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{CITY_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_city(self):
        city_creating_payload = {
            "city_name": "Lviv",
            "country_id": 1,
            "city_latitude": 18,
            "city_longitude": 23,
            "details": "One of the most beautiful cities of Ukraine"
        }

        create_response = self.client.post(f'{CITY_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=city_creating_payload)

        self.assertStatus(create_response, 201)

        created_city = create_response.json
        city_id = created_city['id']

        get_response = self.client.get(f'{CITY_API}/{city_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)
        assert get_response.json == created_city
        assert get_response.json == {**{'id': city_id}, **city_creating_payload}

        city_updating_payload = {
            "city_name": "London",
            "country_id": 2,
            "city_latitude": 34,
            "city_longitude": 56,
            "details": "London is the capital and largest city of England"
        }

        self.assert_200(self.client.put(f'{CITY_API}/{city_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=city_updating_payload))

        get_response_after_update = self.client.get(f'{CITY_API}/{city_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)
        assert get_response_after_update.json == {**{'id': city_id}, **city_updating_payload}

        self.assertStatus(self.client.delete(f'{CITY_API}/{city_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{CITY_API}/{city_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{CITY_API}/{city_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=city_updating_payload))
        self.assert_404(self.client.delete(f'{CITY_API}/{city_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    '''
    Unit tests for Transportations
    '''

    def test_post_transportation__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TRANSPORTATION_API}/post'))

    def test_post_transportation__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TRANSPORTATION_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_transportation__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TRANSPORTATION_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_transportation__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TRANSPORTATION_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_transportation__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{TRANSPORTATION_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_transportation__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{TRANSPORTATION_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_transportation__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/1/get'))

    def test_get_transportation__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_transportation__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_transportation__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_transportation__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_transportation_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/get'))

    def test_get_transportation_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_transportation_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_transportation_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_transportation_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{TRANSPORTATION_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_transportation_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{TRANSPORTATION_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_transportation_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{TRANSPORTATION_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_transportation__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TRANSPORTATION_API}/1/update'))

    def test_update_transportation__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TRANSPORTATION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_transportation__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TRANSPORTATION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_transportation__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TRANSPORTATION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_transportation__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{TRANSPORTATION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_transportation__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{TRANSPORTATION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_transportation__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TRANSPORTATION_API}/1/delete'))

    def test_delete_transportation__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TRANSPORTATION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_transportation__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TRANSPORTATION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_transportation__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TRANSPORTATION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_transportation__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{TRANSPORTATION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_transportation__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{TRANSPORTATION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_transportation(self):
        transportation_creating_payload = {
            "tour_id": 1,
            "transport_type": "PLANE",
            "start_time": "2021-09-19",
            "end_time": "2021-09-25",
            "start_city_id": 1,
            "end_city_id": 2,
            "details": "Plane is power!!!"
        }

        create_response = self.client.post(f'{TRANSPORTATION_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=transportation_creating_payload)

        self.assertStatus(create_response, 201)

        created_transportation = create_response.json
        transportation_id = created_transportation['id']

        get_response = self.client.get(f'{TRANSPORTATION_API}/{transportation_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)
        assert get_response.json == created_transportation

        transportation_updating_payload = {
            "tour_id": 1,
            "transport_type": "PLANE",
            "start_time": "2021-09-19",
            "end_time": "2021-09-25",
            "start_city_id": 1,
            "end_city_id": 2,
            "details": "Plane is power!!!"
        }

        self.assert_200(self.client.put(f'{TRANSPORTATION_API}/{transportation_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=transportation_updating_payload))

        get_response_after_update = self.client.get(f'{TRANSPORTATION_API}/{transportation_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)

        self.assertStatus(self.client.delete(f'{TRANSPORTATION_API}/{transportation_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{TRANSPORTATION_API}/{transportation_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{TRANSPORTATION_API}/{transportation_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=transportation_updating_payload))
        self.assert_404(self.client.delete(f'{TRANSPORTATION_API}/{transportation_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    '''
    Unit tests for Customer_address
    '''

    def test_post_customer_address__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_ADDRESS_API}/post'))

    def test_post_customer_address__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_ADDRESS_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_customer_address__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_ADDRESS_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_customer_address__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_ADDRESS_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_customer_address__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{CUSTOMER_ADDRESS_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_customer_address__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{CUSTOMER_ADDRESS_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_customer_address__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/1/get'))

    def test_get_customer_address__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_customer_address__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_customer_address__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_customer_address__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_customer_address_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/get'))

    def test_get_customer_address_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_customer_address_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_customer_address_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_customer_address_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{CUSTOMER_ADDRESS_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_customer_address_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{CUSTOMER_ADDRESS_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_customer_address_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{CUSTOMER_ADDRESS_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_customer_address__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_ADDRESS_API}/1/update'))

    def test_update_customer_address__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_ADDRESS_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_customer_address__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_ADDRESS_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_customer_address__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_ADDRESS_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_customer_address__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{CUSTOMER_ADDRESS_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_customer_address__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{CUSTOMER_ADDRESS_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_customer_address__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_ADDRESS_API}/1/delete'))

    def test_delete_customer_address__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_ADDRESS_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_customer_address__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_ADDRESS_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_customer_address__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_ADDRESS_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_customer_address__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{CUSTOMER_ADDRESS_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_customer_address__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{CUSTOMER_ADDRESS_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_customer_address(self):
        customer_creating_payload = {
            "username": uuid.uuid4().hex,
            "first_name": "Julia",
            "middle_name": "Bogdanivna",
            "last_name": "Zanevych",
            "phone": "0731213007",
            "date_of_birthday": "2002-07-14",
            "gender": "FEMALE",
            "is_covid_vaccinated": True,
            "is_blocked": True,
            "password_hash": uuid.uuid4().hex,
            "role_id": 1
        }

        create_customer_response = self.client.post(f'{CUSTOMER_API}/post',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                                    json=customer_creating_payload)

        self.assertStatus(create_customer_response, 201)

        created_customer = create_customer_response.json
        customer_id = created_customer['id']

        customer_address_creating_payload = {
            "customer_id": customer_id,
            "city_id": 1,
            "zip_code": "78AO1",
            "street": "Ivan Mazepa",
            "house_number": "9A",
            "apartment_number": 9
        }

        create_response = self.client.post(f'{CUSTOMER_ADDRESS_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=customer_address_creating_payload)

        self.assertStatus(create_response, 201)

        created_customer_address = create_response.json
        customer_address_id = created_customer_address['id']

        get_response = self.client.get(f'{CUSTOMER_ADDRESS_API}/{customer_address_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)
        assert get_response.json == created_customer_address

        customer_address_updating_payload = {
            "customer_id": customer_id,
            "city_id": 1,
            "zip_code": "78AO132",
            "street": "Ivan Mazepa",
            "house_number": "9t",
            "apartment_number": 9
        }

        self.assert_200(self.client.put(f'{CUSTOMER_ADDRESS_API}/{customer_address_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=customer_address_updating_payload))

        get_response_after_update = self.client.get(f'{CUSTOMER_ADDRESS_API}/{customer_address_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)

        self.assertStatus(self.client.delete(f'{CUSTOMER_ADDRESS_API}/{customer_address_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{CUSTOMER_ADDRESS_API}/{customer_address_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{CUSTOMER_ADDRESS_API}/{customer_address_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=customer_address_updating_payload))
        self.assert_404(self.client.delete(f'{CUSTOMER_ADDRESS_API}/{customer_address_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    '''
    Unit tests for Hotels
    '''

    def test_post_hotel__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{HOTEL_API}/post'))

    def test_post_hotel__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{HOTEL_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_hotel__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{HOTEL_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_hotel__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{HOTEL_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_hotel__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{HOTEL_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_hotel__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{HOTEL_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_hotel__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/1/get'))

    def test_get_hotel__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_hotel__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_hotel__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_hotel__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_hotel_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/get'))

    def test_get_hotel_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_hotel_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_hotel_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_hotel_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{HOTEL_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_hotel_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{HOTEL_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_hotel_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{HOTEL_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_hotel__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{HOTEL_API}/1/update'))

    def test_update_hotel__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{HOTEL_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_hotel__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{HOTEL_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_hotel__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{HOTEL_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_hotel__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{HOTEL_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_hotel__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{HOTEL_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_hotel__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{HOTEL_API}/1/delete'))

    def test_delete_hotel__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{HOTEL_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_hotel__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{HOTEL_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_hotel__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{HOTEL_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_hotel__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{HOTEL_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_hotel__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{HOTEL_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_hotel(self):
        hotel_creating_payload = {
            "name": "Grand",
            "hotel_class": "USUAL",
            "city_id": 1,
            "is_animals_allowed": True,
            "details": "The best place!!!"
        }

        create_response = self.client.post(f'{HOTEL_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=hotel_creating_payload)

        self.assertStatus(create_response, 201)

        created_hotel = create_response.json
        hotel_id = created_hotel['id']

        get_response = self.client.get(f'{HOTEL_API}/{hotel_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)
        assert get_response.json == created_hotel
        assert get_response.json == {**{'id': hotel_id}, **hotel_creating_payload}

        hotel_updating_payload = {
            "name": "Grand",
            "hotel_class": "USUAL",
            "city_id": 1,
            "is_animals_allowed": True,
            "details": "The best place!!!"
        }

        self.assert_200(self.client.put(f'{HOTEL_API}/{hotel_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=hotel_updating_payload))

        get_response_after_update = self.client.get(f'{HOTEL_API}/{hotel_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)
        assert get_response_after_update.json == {**{'id': hotel_id}, **hotel_updating_payload}

        self.assertStatus(self.client.delete(f'{HOTEL_API}/{hotel_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{HOTEL_API}/{hotel_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{HOTEL_API}/{hotel_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=hotel_updating_payload))
        self.assert_404(self.client.delete(f'{HOTEL_API}/{hotel_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    '''
    Unit tests for Vouchers
    '''

    def test_post_voucher__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{VOUCHER_API}/post'))

    def test_post_voucher__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{VOUCHER_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_voucher__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{VOUCHER_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_voucher__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{VOUCHER_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_voucher__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{VOUCHER_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_voucher__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{VOUCHER_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_voucher__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/1/get'))

    def test_get_voucher__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_voucher__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_voucher__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_voucher__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_voucher_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/get'))

    def test_get_voucher_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_voucher_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_voucher_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_voucher_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{VOUCHER_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_voucher_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{VOUCHER_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_voucher_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{VOUCHER_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_voucher__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{VOUCHER_API}/1/update'))

    def test_update_voucher__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{VOUCHER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_voucher__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{VOUCHER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_voucher__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{VOUCHER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_voucher__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{VOUCHER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_voucher__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{VOUCHER_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_voucher__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{VOUCHER_API}/1/delete'))

    def test_delete_voucher__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{VOUCHER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_voucher__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{VOUCHER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_voucher__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{VOUCHER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_voucher__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{VOUCHER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_voucher__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{VOUCHER_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_voucher(self):
        voucher_creating_payload = {
            "tour_id": 1,
            "customer_ids": [
                1,
                2,
                3,
                4
            ]
        }

        create_response = self.client.post(f'{VOUCHER_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=voucher_creating_payload)

        self.assertStatus(create_response, 201)

        created_voucher = create_response.json
        voucher_id = created_voucher['id']

        get_response = self.client.get(f'{VOUCHER_API}/{voucher_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)
        assert get_response.json == created_voucher
        assert get_response.json == {**{'id': voucher_id}, **voucher_creating_payload}

        voucher_updating_payload = {
            "tour_id": 1,
            "customer_ids": [
                3,
                4,
                5,
                6
            ]
        }

        self.assert_200(self.client.put(f'{VOUCHER_API}/{voucher_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=voucher_updating_payload))

        get_response_after_update = self.client.get(f'{VOUCHER_API}/{voucher_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)
        assert get_response_after_update.json == {**{'id': voucher_id}, **voucher_updating_payload}

        self.assertStatus(self.client.delete(f'{VOUCHER_API}/{voucher_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{VOUCHER_API}/{voucher_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{VOUCHER_API}/{voucher_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=voucher_updating_payload))
        self.assert_404(self.client.delete(f'{VOUCHER_API}/{voucher_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    '''
    Unit tests for Permissions
    '''

    def test_post_permission__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{PERMISSION_API}/post'))

    def test_post_permission__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{PERMISSION_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_permission__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{PERMISSION_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_permission__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{PERMISSION_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_permission__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{PERMISSION_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_permission__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{PERMISSION_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_permission__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/1/get'))

    def test_get_permission__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_permission__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_permission__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_permission__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_permission_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/get'))

    def test_get_permission_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_permission_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_permission_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_permission_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{PERMISSION_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_permission_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{PERMISSION_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_permission_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{PERMISSION_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_permission__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{PERMISSION_API}/1/update'))

    def test_update_permission__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{PERMISSION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_permission__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{PERMISSION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_permission__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{PERMISSION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_permission__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{PERMISSION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_permission__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{PERMISSION_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_permission__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{PERMISSION_API}/1/delete'))

    def test_delete_permission__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{PERMISSION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_permission__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{PERMISSION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_permission__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{PERMISSION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_permission__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{PERMISSION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_permission__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{PERMISSION_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_permission(self):
        permission_creating_payload = {
            "method": "GET_CUSTOMERS_LIST"
        }

        create_response = self.client.post(f'{PERMISSION_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=permission_creating_payload)

        self.assertStatus(create_response, 201)

        created_permission = create_response.json
        permission_id = created_permission['id']

        get_response = self.client.get(f'{PERMISSION_API}/{permission_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)

        assert get_response.json == {**{'id': permission_id}, **permission_creating_payload}

        permission_updating_payload = {
            "method": "GET_CUSTOMERS_LIST"
        }

        self.assert_200(self.client.put(f'{PERMISSION_API}/{permission_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=permission_updating_payload))

        get_response_after_update = self.client.get(f'{PERMISSION_API}/{permission_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)
        assert get_response_after_update.json == {**{'id': permission_id}, **permission_updating_payload}

        self.assertStatus(self.client.delete(f'{PERMISSION_API}/{permission_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{PERMISSION_API}/{permission_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{PERMISSION_API}/{permission_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=permission_updating_payload))
        self.assert_404(self.client.delete(f'{PERMISSION_API}/{permission_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    '''
    Unit tests for Roles
    '''

    def test_post_role__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{ROLE_API}/post'))

    def test_post_role__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{ROLE_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_post_role__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{ROLE_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_post_role__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{ROLE_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_role__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.post(f'{ROLE_API}/post',
                                         headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_post_role__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.post(f'{ROLE_API}/post',
                                         headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_role__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/1/get'))

    def test_get_role__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_role__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_role__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_role__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/1/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_role_list__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/get'))

    def test_get_role_list__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_get_role_list__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_get_role_list__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_role_list__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.get(f'{ROLE_API}/get',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_get_role_list__when_non_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{ROLE_API}/get',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_get_role_list__when_admin_user__expect_200(self):
        self.assert_200(self.client.get(f'{ROLE_API}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))

    def test_update_role__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{ROLE_API}/1/update'))

    def test_update_role__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{ROLE_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_update_role__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{ROLE_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_update_role__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{ROLE_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_role__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.put(f'{ROLE_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_update_role__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.put(f'{ROLE_API}/1/update',
                                        headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_delete_role__when_missed_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{ROLE_API}/1/delete'))

    def test_delete_role__when_invalid_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{ROLE_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_AUTHORIZATION_HEADER}))

    def test_delete_role__when_non_basic_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{ROLE_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_BASIC_AUTHORIZATION_HEADER}))

    def test_delete_role__when_invalid_base64_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{ROLE_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_BASE64_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_role__when_invalid_payload_authorization_header__expect_401(self):
        self.assert_401(self.client.delete(f'{ROLE_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: INVALID_PAYLOAD_AUTHORIZATION_HEADER}))

    def test_delete_role__when_non_admin_user__expect_403(self):
        self.assert_403(self.client.delete(f'{ROLE_API}/1/delete',
                                           headers={AUTHORIZATION_HEADER: NON_ADMIN_AUTHORIZATION_HEADER}))

    def test_crud_role(self):
        permission_ids = []
        for i in range(3):
            permission_creating_payload = {
                "method": uuid.uuid4().hex
            }

            create_permission1_response = self.client.post(f'{PERMISSION_API}/post',
                                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                                           json=permission_creating_payload)

            self.assertStatus(create_permission1_response, 201)

            created_permission = create_permission1_response.json
            permission_id = created_permission['id']

            permission_ids.append(permission_id)

        role_creating_payload = {
            "name": uuid.uuid4().hex,
            "permission_ids": permission_ids
        }

        create_response = self.client.post(f'{ROLE_API}/post',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                           json=role_creating_payload)

        self.assertStatus(create_response, 201)

        created_role = create_response.json
        role_id = created_role['id']

        get_response = self.client.get(f'{ROLE_API}/{role_id}/get',
                                       headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response)
        assert get_response.json == created_role
        assert get_response.json == {**{'id': role_id}, **role_creating_payload}

        del permission_ids[0]
        del permission_ids[1]
        for i in range(3):
            permission_creating_payload = {
                "method": uuid.uuid4().hex
            }

            create_permission1_response = self.client.post(f'{PERMISSION_API}/post',
                                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                                           json=permission_creating_payload)

            self.assertStatus(create_permission1_response, 201)

            created_permission = create_permission1_response.json
            permission_id = created_permission['id']

            permission_ids.append(permission_id)

        role_updating_payload = {
            "name": uuid.uuid4().hex,
            "permission_ids": permission_ids
        }

        self.assert_200(self.client.put(f'{ROLE_API}/{role_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=role_updating_payload))

        get_response_after_update = self.client.get(f'{ROLE_API}/{role_id}/get',
                                                    headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER})

        self.assert_200(get_response_after_update)
        assert get_response_after_update.json == {**{'id': role_id}, **role_updating_payload}

        self.assertStatus(self.client.delete(f'{ROLE_API}/{role_id}/delete',
                                             headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}),
                          204)

        self.assert_404(self.client.get(f'{ROLE_API}/{role_id}/get',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))
        self.assert_404(self.client.put(f'{ROLE_API}/{role_id}/update',
                                        headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER},
                                        json=role_updating_payload))
        self.assert_404(self.client.delete(f'{ROLE_API}/{role_id}/delete',
                                           headers={AUTHORIZATION_HEADER: ADMIN_AUTHORIZATION_HEADER}))


if __name__ == '__main__':
    unittest.main()
