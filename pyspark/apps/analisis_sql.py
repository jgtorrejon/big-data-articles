# Aplicación PySpark que utiliza Spark SQL para analizar datos desde un CSV.
from pyspark.sql import SparkSession


def main():
    """
    Punto de entrada de la aplicación Spark.
    """
    spark = SparkSession.builder \
        .appName("AnalisisConSparkSQL") \
        .master("spark://spark-master:7077") \
        .getOrCreate()
    print(">>> SparkSession iniciada correctamente.")
    # 1. Cargar los datos desde el archivo CSV en un DataFrame
    ruta_csv = "/opt/bitnami/spark/data/empleados.csv"
    df = spark.read.csv(ruta_csv, header=True, inferSchema=True)
    # 2. Registrar el DataFrame como una Vista Temporal SQL
    # Este paso permite que el DataFrame sea consultado con SQL bajo el nombre "empleados_vista".
    df.createOrReplaceTempView("empleados_vista")
    print(">>> DataFrame registrado como la vista temporal 'empleados_vista'.")
    # 3. Definir y ejecutar la consulta SQL
    query_sql = """
        SELECT
        departamento
        AVG(salario) AS salario_promedio,
        COUNT(*) AS numero_de_empleados
        FROM
        empleados_vista
        GROUP BY
        departamento
        ORDER BY
        salario_promedio DESC
    """
    print(f">>> Ejecutando la siguiente consulta SQL:\n{query_sql}")
    # spark.sql() ejecuta la consulta y devuelve el resultado como un nuevo DataFrame.
    resultado_df = spark.sql(query_sql)
    # 4. Mostrar el resultado del análisis
    print(">>> Resultado del análisis obtenido con Spark SQL:")
    resultado_df.show()
    # 5. Detener la SparkSession para liberar los recursos del clúster
    spark.stop()
    print(">>> SparkSession detenida. Proceso finalizado.")


if __name__ == '__main__':
    main()
