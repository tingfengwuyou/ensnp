import multiprocessing
import time

def calculate_expression(expression):
    start_time = time.time()  # 记录开始时间
    result = eval(expression)  # 计算表达式
    end_time = time.time()  # 记录结束时间
    execution_time = end_time - start_time  # 计算执行时间
    return result, execution_time

if __name__ == '__main__':
    expressions = ['2 + 3', '4 * 5', '6 / 2']

    processes = []
    results = []

    for expression in expressions:
        process = multiprocessing.Process(target=calculate_expression, args=(expression,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    for i, expression in enumerate(expressions):
        result, execution_time = calculate_expression(expression)
        results.append(result)
        print(f'Result of "{expression}": {result}, Execution Time: {execution_time} seconds')