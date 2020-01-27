#  Copyright (c) 2020. This code has been written by Andrei Izbavitelev

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')
