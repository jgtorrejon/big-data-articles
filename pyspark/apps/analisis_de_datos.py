# Aplicación PySpark que calcula el salario promedio por departamento.
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg


def main():
    """
    Punto de entrada de la aplicación Spark.
    """
    # 1. Crear la SparkSession
    spark = SparkSession.builder.appName("AnalisisSalariosDocker") \
        .master("spark://spark-master:7077") \
        .getOrCreate()
    print(">>> SparkSession iniciada correctamente.")
    # 2. Cargar los datos
    datos_empleados = [
        ("Ventas", "Juan", 3200),
        ("Ventas", "Ana", 3500),
        ("Tecnologia", "Carlos", 5500),
        ("Tecnologia", "Maria", 6200),
        ("Tecnologia", "Pedro", 5800),
        ("Marketing", "Sofia", 4100),
        ("Marketing", "Luis", 4300)
    ]
    columnas = ["departamento", "nombre", "salario"]
    df = spark.createDataFrame(datos_empleados, schema=columnas)
    print(">>> DataFrame original:")
    df.show()
    # 3. Realizar la transformación
    # Agrupamos por 'departamento' y calculamos el salario promedio.
    salario_promedio_df = df.groupBy("departamento") \
        .agg(avg("salario").alias("salario_promedio"))
    print(">>> Resultado del análisis (Salario promedio por departamento):")
    salario_promedio_df.show()
    # 4. Detener la SparkSession para liberar recursos del clúster
    spark.stop()
    print(">>> SparkSession detenida. Proceso finalizado.")


if __name__ == '__main__':
    main()
