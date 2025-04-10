import sender_stand_request
import data

def get_new_kit(names):
    current_body = data.kit_body.copy()
    current_body["name"] = names
    return current_body
def positive_assert(names):
    kit_body = get_new_kit(names)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.authtoken)
    assert kit_response.status_code == 201

def negative_assert_symbol(namess):

    kit_body = get_new_kit(namess)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.authtoken)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] ==  "No se han aprobado todos los parámetros requeridos"

def test_create_kit_1_letter_in_camp_name_get_success_response():
    positive_assert(data.kit_name_1_char)
def test_create_kit_511_letter_in_camp_name_get_success_response():
    positive_assert(data.kit_name_511_char)
def test_create_kit_0_letter_in_camp_name_get_negative_response():
    negative_assert_symbol(data.kit_name_0_char)
def test_create_kit_512_letter_in_camp_name_get_negative_response():
    negative_assert_symbol(data.kit_name_512_char)
def test_create_kit_special_letter_in_camp_name_get_success_response():
    positive_assert (data.kit_name_special_char)
def test_create_kit_space_btw_letter_in_camp_name_get_success_response():
    positive_assert (data.kit_space_btw_char)
def test_create_kit_number_in_camp_name_get_success_response():
    positive_assert(data.kit_dif_number_in_camp_name)
def test_create_kit_empty_in_camp_name_get_success_response():
    negative_assert_symbol(data.kit_name_empty_in_camp_name)
def test_create_kit_dif_number_in_camp_name_get_success_response():
    negative_assert_symbol(data.kit_dif_number_in_camp_name)






